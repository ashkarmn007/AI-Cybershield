import ipaddress
import re
import urllib.request
from bs4 import BeautifulSoup
import socket
import requests
from googlesearch import search
import whois
from datetime import datetime, date

socket.setdefaulttimeout(5)


def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month


def generate_data_set(url):
    print(url, 'in fext')
    print('entered feature extraction')

    data_set = []

    # URL Standardization
    if not re.match(r"^https?", url):
        url = "http://" + url

    # Request
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
    except:
        response = ""
        soup = -999

    # Domain
    try:
        domain = re.findall(r"://([^/]+)/?", url)[0]
    except:
        domain = url

    if domain.startswith("www."):
        domain = domain.replace("www.", "")

    # WHOIS
    try:
        whois_response = whois.whois(domain)
    except:
        whois_response = None

    # Page Rank
    try:
        rank_checker_response = requests.post(
            "https://www.checkpagerank.net/index.php",
            {"name": domain},
            timeout=5
        )
        global_rank = int(re.findall(r"Global Rank: ([0-9]+)", rank_checker_response.text)[0])
    except:
        global_rank = -1

    # 1 IP
    try:
        ipaddress.ip_address(url)
        data_set.append(-1)
    except:
        data_set.append(1)

    # 2 Length
    if len(url) < 54:
        data_set.append(1)
    elif len(url) <= 75:
        data_set.append(0)
    else:
        data_set.append(-1)

    # 3 Shortening
    data_set.append(-1 if re.search('bit\.ly|tinyurl|qr\.co|ow\.ly', url) else 1)

    # 4 @
    data_set.append(-1 if "@" in url else 1)

    # 5 //
    lst = [x.start() for x in re.finditer('//', url)]
    data_set.append(-1 if len(lst) > 1 and lst[-1] > 6 else 1)

    # 6 Prefix
    data_set.append(-1 if re.findall(r"https?://[^\-]+-[^\-]+/", url) else 1)

    # 7 Subdomain
    dots = url.count('.')
    data_set.append(1 if dots == 1 else 0 if dots == 2 else -1)

    # 8 SSL
    if response != "" and hasattr(response, "text") and response.text:
        data_set.append(1)
    else:
        data_set.append(-1)

    # 9 Domain age
    try:
        exp = whois_response.expiration_date
        if isinstance(exp, list):
            exp = exp[0]
        reg_len = (exp - datetime.today()).days
        data_set.append(1 if reg_len > 365 else -1)
    except:
        data_set.append(-1)

    # 10 Favicon
    if soup == -999:
        data_set.append(-1)
    else:
        added = False
        for link in soup.find_all('link', href=True):
            if domain in link['href'] or url in link['href']:
                data_set.append(1)
            else:
                data_set.append(-1)
            added = True
            break
        if not added:
            data_set.append(-1)

    # 11 Port
    data_set.append(-1 if ":" in domain else 1)

    # 12 HTTPS
    data_set.append(1 if url.startswith("https") else -1)

    # 13 Request URL
    if soup == -999:
        data_set.append(-1)
    else:
        total, success = 0, 0
        for tag in soup.find_all(['img', 'iframe'], src=True):
            total += 1
            if domain in tag['src']:
                success += 1
        try:
            pct = success / total * 100
            data_set.append(1 if pct < 22 else 0 if pct < 61 else -1)
        except:
            data_set.append(1)

    # 14 Anchor
    if soup == -999:
        data_set.append(-1)
    else:
        total, unsafe = 0, 0
        for a in soup.find_all('a', href=True):
            total += 1
            if "#" in a['href'] or "javascript" in a['href']:
                unsafe += 1
        try:
            pct = unsafe / total * 100
            data_set.append(1 if pct < 31 else 0 if pct < 67 else -1)
        except:
            data_set.append(1)

    # 15 Links
    if soup == -999:
        data_set.append(-1)
    else:
        data_set.append(1)

    # 16 SFH (FIXED)
    if soup == -999:
        data_set.append(-1)
    else:
        added = False
        for form in soup.find_all('form', action=True):
            action = form['action']
            if action == "" or action == "about:blank":
                data_set.append(-1)
            elif domain not in action:
                data_set.append(0)
            else:
                data_set.append(1)
            added = True
            break
        if not added:
            data_set.append(-1)

    # 17 Email
    if response == "":
        data_set.append(-1)
    else:
        data_set.append(1 if "mailto" in response.text else -1)

    # 18 Abnormal
    data_set.append(-1 if response != "" else 1)

    # 19 Redirect
    if response == "":
        data_set.append(-1)
    else:
        data_set.append(1 if len(response.history) > 2 else -1)

    # 20 Mouseover
    data_set.append(-1)

    # 21 Right click
    data_set.append(-1)

    # 22 Popup
    data_set.append(1 if response != "" and "alert(" in response.text else -1)

    # 23 iframe
    data_set.append(1 if response != "" and "<iframe" in response.text else -1)

    # 24 Age
    try:
        reg = whois_response.creation_date
        if isinstance(reg, list):
            reg = reg[0]
        age = diff_month(date.today(), reg.date())
        data_set.append(1 if age < 6 else -1)
    except:
        data_set.append(1)

    # 25 DNS
    data_set.append(1 if whois_response else -1)

    # 26 Traffic
    data_set.append(-1)

    # 27 Page rank
    data_set.append(-1 if global_rank < 100000 and global_rank != -1 else 1)

    # 28 Google index
    try:
        data_set.append(1 if list(search(url, num_results=3)) else -1)
    except:
        data_set.append(-1)

    # 29 Links count
    if response == "":
        data_set.append(-1)
    else:
        count = response.text.count("<a href=")
        data_set.append(1 if count == 0 else 0 if count <= 2 else -1)

    # 30 Statistical
    try:
        ip = socket.gethostbyname(domain)
        data_set.append(-1 if re.search('146\.112|213\.174', ip) else 1)
    except:
        data_set.append(-1)

    # FINAL CHECK
    print("TOTAL FEATURES:", len(data_set))

    if len(data_set) != 30:
        print("ERROR → Feature mismatch, fixing...")
        while len(data_set) < 30:
            data_set.append(-1)
        data_set = data_set[:30]

    return data_set