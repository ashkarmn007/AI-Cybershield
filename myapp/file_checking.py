
import hashlib
import requests
import os

# ===== CONFIGURATION =====
VT_API_KEY = 'aa7a2ae368ab746bfbcef91634d1d348aa8841a9031fdae83e6789290c8f81b0'  # Replace with your API key
VT_URL = 'https://www.virustotal.com/api/v3/files/'

# ===== FUNCTION TO CALCULATE FILE HASH =====
def get_file_hash(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        chunk = f.read(8192)
        while chunk:
            hasher.update(chunk)
            chunk = f.read(8192)
    return hasher.hexdigest()

# ===== FUNCTION TO UPLOAD FILE TO VIRUSTOTAL =====
def upload_file_to_virustotal(file_path):
    url = "https://www.virustotal.com/api/v3/files"
    headers = {
        "x-apikey": VT_API_KEY
    }
    with open(file_path, "rb") as f:
        files = {"file": (os.path.basename(file_path), f)}
        response = requests.post(url, files=files, headers=headers)
    print("=====================================")
    print(response)
    if response.status_code == 200:
        data = response.json()
        analysis_id = data["data"]["id"]
        print(f"[+] File uploaded successfully. Analysis ID: {analysis_id}")
        return f"https://www.virustotal.com/gui/file-analysis/{analysis_id}"
    else:
        print(f"[!] Upload failed with status code {response.status_code}")
        print(response.text)
        return None

# ===== CHECK FILE HASH AGAINST VIRUSTOTAL =====
def check_virustotal(file_hash, file_path):
    headers = {
        "x-apikey": VT_API_KEY
    }
    response = requests.get(VT_URL + file_hash, headers=headers)
    print("====================================")
    print(response)
    if response.status_code == 200:
        data = response.json()
        stats = data.get("data", {}).get("attributes", {}).get("last_analysis_stats", {})
        return stats

    elif response.status_code == 404:
        print("[*] File not found in VirusTotal. Uploading it now...")
        upload_result = upload_file_to_virustotal(file_path)
        if upload_result:
            return f"File uploaded. You can monitor analysis here:\n{upload_result}"
        else:
            return "Upload failed."

    else:
        return f"Error: {response.status_code}"

# ===== STATIC SUSPICIOUS STRING CHECK =====
def scan_suspicious_content(file_path):
    suspicious_patterns = [
        b'cmd.exe', b'powershell', b'base64', b'CreateRemoteThread', b'VirtualAlloc',
        b'ShellExecute', b'GetProcAddress', b'LoadLibrary', b'0xE8', b'0xFF'
    ]
    results = []
    with open(file_path, 'rb') as f:
        content = f.read()
        for pattern in suspicious_patterns:
            if pattern in content:
                results.append(pattern.decode('utf-8', errors='ignore'))
    return results

# ===== MAIN FUNCTION =====
def file_checking_main(file_path):
    if not os.path.isfile(file_path):
        print("[!] File not found.")
        return

    print(f"[*] Analyzing: {file_path}")
    file_hash = get_file_hash(file_path)
    print(f"[*] SHA256: {file_hash}")

    print("\n[*] Checking VirusTotal...")
    vt_result = check_virustotal(file_hash, file_path)
    print(f"[+] VirusTotal Result: {vt_result}")

    print("\n[*] Performing Static Analysis...")
    suspicious = scan_suspicious_content(file_path)
    if suspicious:
         print(f"[!] Suspicious Strings Found: {suspicious}")
         return (f"Suspicious Strings Found: {suspicious}")
    else:
        print("[+] No suspicious strings found.")
        return("No suspicious in this file.")



import requests
def check_leakcheck(email):
    url = f"https://leakcheck.io/api/public?check={email}"
    headers = {'User-Agent': 'Gmail-Breach-Checker'}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        print(response)
        if response.status_code == 200:
            data = response.json()
            if data.get("found"):
                print(f"🔐 '{email}' was found in known data leaks.")
            else:
                print(f"✅ '{email}' was not found in public breaches.")
        else:
            print(f"❌ Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ Request failed: {e}")
