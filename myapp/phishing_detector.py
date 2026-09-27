# import re
# import socket
# import requests
# from urllib.parse import urlparse
# import whois
# from datetime import datetime
#
# SUSPICIOUS_KEYWORDS = [
#     "login", "verify", "secure", "account", "bank",
#     "signin", "update", "confirm", "password", "otp"
# ]
#
# def detect_phishing(url):
#     score = 0
#
#     # Normalize URL
#     if not url.startswith("http"):
#         url = "http://" + url
#
#     parsed = urlparse(url)
#     domain = parsed.netloc.lower()
#
#     # 1️⃣ IP address in URL
#     try:
#         socket.inet_aton(domain)
#         score += 3
#     except:
#         pass
#
#     # 2️⃣ URL length
#     if len(url) > 75:
#         score += 1
#
#     # 3️⃣ @ symbol
#     if "@" in url:
#         score += 3
#
#     # 4️⃣ Hyphen in domain
#     if "-" in domain:
#         score += 1
#
#     # 5️⃣ Suspicious keywords
#     keyword_count = 0
#     for word in SUSPICIOUS_KEYWORDS:
#         if word in url.lower():
#             keyword_count += 1
#
#     if keyword_count >= 2:
#         score += 3
#     elif keyword_count == 1:
#         score += 1
#
#     # 6️⃣ HTTPS check
#     if not url.startswith("https"):
#         score += 1
#
#     # 7️⃣ Domain age check
#     try:
#         domain_info = whois.whois(domain)
#         creation_date = domain_info.creation_date
#
#         if isinstance(creation_date, list):
#             creation_date = creation_date[0]
#
#         domain_age_days = (datetime.now() - creation_date).days
#
#         if domain_age_days < 180:
#             score += 3
#     except:
#         score += 1
#
#     # 8️⃣ Webpage content check
#     try:
#         r = requests.get(url, timeout=5)
#         page_text = r.text.lower()
#
#         if "password" in page_text or "otp" in page_text:
#             score += 1
#     except:
#         score += 1
#
#     # 🔥 FINAL DECISION
#     if score >= 4:
#         return "This is Phishing"
#     else:
#         return "Normal"














import ipaddress
import re
import urllib.request
from bs4 import BeautifulSoup
import socket
import requests
from googlesearch import search
import whois
from datetime import datetime, date
import time
from dateutil.parser import parse as date_parse


def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month


def generate_data_set(url):

    data_set = []

    # URL Standardization
    if not re.match(r"^https?", url):
        url = "http://" + url

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
    except:
        response = ""
        soup = -999

    # Extract Domain
    domain = re.findall(r"://([^/]+)/?", url)[0]
    if domain.startswith("www."):
        domain = domain.replace("www.", "")

    # WHOIS Data
    try:
        whois_response = whois.whois(domain)
    except:
        whois_response = ""

    # Page rank checker (checkpagerank.net)
    try:
        rank_checker_response = requests.post(
            "https://www.checkpagerank.net/index.php",
            {"name": domain}
        )
        global_rank = int(re.findall(r"Global Rank: ([0-9]+)", rank_checker_response.text)[0])
    except:
        global_rank = -1

    # 1. IP Address
    try:
        ipaddress.ip_address(url)
        data_set.append(-1)
    except:
        data_set.append(1)

    # 2. URL Length
    if len(url) < 54:
        data_set.append(1)
    elif len(url) <= 75:
        data_set.append(0)
    else:
        data_set.append(-1)

    # 3. Shortening Services
    match = re.search(
        'bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|'
        'yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|'
        'short\.to|budurl\.com|ping\.fm|post\.ly|just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|'
        'doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|lnkd\.in|'
        'db\.tt|qr\.ae|adf\.ly|bitly\.com|cur\.lv|ity\.im|q\.gs|po\.st|bc\.vc|u\.to|j\.mp|'
        'buzurl\.com|cutt\.us|u\.bb|yourls\.org|x\.co|scrnch\.me|vzturl\.com|qr\.net|v\.gd',
        url
    )
    data_set.append(-1 if match else 1)

    # 4. @ Symbol
    data_set.append(-1 if "@" in url else 1)

    # 5. Double Slash Redirecting
    lst = [x.start() for x in re.finditer('//', url)]
    data_set.append(-1 if lst[-1] > 6 else 1)

    # 6. Prefix-Suffix
    data_set.append(-1 if re.findall(r"https?://[^\-]+-[^\-]+/", url) else 1)

    # 7. Subdomain
    dot_count = len(re.findall("\.", url))
    if dot_count == 1:
        data_set.append(1)
    elif dot_count == 2:
        data_set.append(0)
    else:
        data_set.append(-1)

    # 8. SSL Final State
    try:
        if response.text:
            data_set.append(1)
    except:
        data_set.append(-1)

    # 9. Domain Registration Length
    try:
        expiration_date = whois_response.expiration_date
        expiration_date = min(expiration_date)
        today = datetime.today()
        registration_length = abs((expiration_date - today).days)

        if registration_length / 365 <= 1:
            data_set.append(-1)
        else:
            data_set.append(1)
    except:
        data_set.append(-1)

    # 10. Favicon
    if soup == -999:
        data_set.append(-1)
    else:
        try:
            for head in soup.find_all('head'):
                for link in soup.find_all('link', href=True):
                    dots = [x.start() for x in re.finditer('\.', link['href'])]
                    if url in link['href'] or domain in link['href'] or len(dots) == 1:
                        data_set.append(1)
                        raise StopIteration
                    else:
                        data_set.append(-1)
                        raise StopIteration
        except StopIteration:
            pass

    # 11. Port
    try:
        port = domain.split(":")[1]
        data_set.append(-1 if port else 1)
    except:
        data_set.append(1)

    # 12. HTTPS Token
    data_set.append(1 if url.startswith("https://") else -1)

    # 13. Request URL
    i = 0
    success = 0
    if soup != -999:
        for tag in soup.find_all(['img', 'audio', 'embed', 'iframe'], src=True):
            dots = [x.start() for x in re.finditer('\.', tag['src'])]
            if url in tag['src'] or domain in tag['src'] or len(dots) == 1:
                success += 1
            i += 1

        try:
            percentage = success / float(i) * 100
            if percentage < 22.0:
                data_set.append(1)
            elif percentage < 61.0:
                data_set.append(0)
            else:
                data_set.append(-1)
        except:
            data_set.append(1)
    else:
        data_set.append(-1)

    # 14. URL of Anchor
    if soup == -999:
        data_set.append(-1)
    else:
        unsafe = 0
        i = 0
        for a in soup.find_all('a', href=True):
            if "#" in a['href'] or "javascript" in a['href'].lower() or "mailto" in a['href'].lower() or not (url in a['href'] or domain in a['href']):
                unsafe += 1
            i += 1

        try:
            percentage = unsafe / float(i) * 100
        except:
            percentage = 0

        if percentage < 31:
            data_set.append(1)
        elif percentage < 67:
            data_set.append(0)
        else:
            data_set.append(-1)

    # 15. Links in Tags
    if soup == -999:
        data_set.append(-1)
    else:
        i = 0
        success = 0
        for link in soup.find_all('link', href=True):
            dots = [x.start() for x in re.finditer('\.', link['href'])]
            if url in link['href'] or domain in link['href'] or len(dots) == 1:
                success += 1
            i += 1

        for script in soup.find_all('script', src=True):
            dots = [x.start() for x in re.finditer('\.', script['src'])]
            if url in script['src'] or domain in script['src'] or len(dots) == 1:
                success += 1
            i += 1

        try:
            percentage = success / float(i) * 100
        except:
            percentage = 0

        if percentage < 17:
            data_set.append(1)
        elif percentage < 81:
            data_set.append(0)
        else:
            data_set.append(-1)

    # 16. SFH
    if soup == -999:
        data_set.append(-1)
    else:
        for form in soup.find_all('form', action=True):
            action = form['action']
            if action == "" or action == "about:blank":
                data_set.append(-1)
            elif url not in action and domain not in action:
                data_set.append(0)
            else:
                data_set.append(1)
            break

    # 17. Submitting to Email
    if response == "":
        data_set.append(-1)
    else:
        data_set.append(1 if re.findall(r"[mail\(\)|mailto:?]", response.text) else -1)

    # 18. Abnormal URL
    if response == "":
        data_set.append(-1)
    else:
        data_set.append(1 if response.text == "" else -1)

    # 19. Redirect
    if response == "":
        data_set.append(-1)
    else:
        if len(response.history) <= 1:
            data_set.append(-1)
        elif len(response.history) <= 4:
            data_set.append(0)
        else:
            data_set.append(1)

    # 20. On Mouseover
    if response == "":
        data_set.append(-1)
    else:
        data_set.append(1 if re.findall("<script>.+onmouseover.+</script>", response.text) else -1)

    # 21. Right Click
    if response == "":
        data_set.append(-1)
    else:
        data_set.append(1 if re.findall(r"event.button ?== ?2", response.text) else -1)

    # 22. Popup Window
    if response == "":
        data_set.append(-1)
    else:
        data_set.append(1 if "alert(" in response.text else -1)

    # 23. Iframe
    if response == "":
        data_set.append(-1)
    else:
        data_set.append(1 if re.findall(r"[<iframe>|<frameBorder>]", response.text) else -1)

    # 24. Age of Domain
    try:
        reg_date = whois_response.creation_date
        if isinstance(reg_date, list):
            reg_date = reg_date[0]
        age = diff_month(date.today(), reg_date.date())
        data_set.append(-1 if age >= 6 else 1)
    except:
        data_set.append(1)

    # 25. DNS Record
    try:
        d = whois.whois(domain)
        if registration_length / 365 <= 1:
            data_set.append(-1)
        else:
            data_set.append(1)
    except:
        data_set.append(-1)

    # 26. Web Traffic (Alexa — deprecated but kept for compatibility)
    try:
        alexa = BeautifulSoup(
            urllib.request.urlopen("http://data.alexa.com/data?cli=10&dat=s&url=" + url).read(),
            "xml"
        )
        rank = int(alexa.find("REACH")['RANK'])
        data_set.append(1 if rank < 100000 else 0)
    except:
        data_set.append(-1)

    # 27. Page Rank
    try:
        if global_rank > 0 and global_rank < 100000:
            data_set.append(-1)
        else:
            data_set.append(1)
    except:
        data_set.append(1)

    # 28. Google Index
    try:
        site = list(search(url, num_results=5))
        data_set.append(1 if site else -1)
    except:
        data_set.append(-1)

    # 29. Links pointing to page
    if response == "":
        data_set.append(-1)
    else:
        num_links = len(re.findall(r"<a href=", response.text))
        if num_links == 0:
            data_set.append(1)
        elif num_links <= 2:
            data_set.append(0)
        else:
            data_set.append(-1)

    # 30. Statistical Report
    url_match = re.search(
        'at\.ua|usa\.cc|baltazarpresentes\.com\.br|pe\.hu|esy\.es|hol\.es|myjino\.ru|96\.lt|ow\.ly',
        url
    )
    try:
        ip_address = socket.gethostbyname(domain)
        ip_match = re.search(
            '146\.112\.61\.108|213\.174\.157\.151|121\.50\.168\.88|192\.185\.217\.116|78\.46\.211\.158|'
            '181\.174\.165\.13',
            ip_address
        )
        if url_match or ip_match:
            data_set.append(-1)
        else:
            data_set.append(1)
    except:
        data_set.append(-1)

    return data_set


# RUN
res = generate_data_set("https://stackoverflow.com")
print(res)
print(len(res))
