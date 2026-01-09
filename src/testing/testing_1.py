import pywifi
import subprocess, re, sys, time

def get_visible_networks():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()
    time.sleep(2)
    results = iface.scan_results()
    networks = {}
    for net in results:
        bssid = net.bssid.lower()
        ssid = net.ssid
        if ssid:
            networks[bssid] = ssid
    return networks

def get_saved_password(ssid):
    try:
        output = subprocess.check_output(
            ["netsh", "wlan", "show", "profile", ssid, "key=clear"],
            stderr=subprocess.DEVNULL
        ).decode(errors="ignore")
    except subprocess.CalledProcessError:
        return None
    m = re.search(r"Key Content\s*:\s*(.+)", output, re.IGNORECASE)
    return m.group(1).strip() if m else None

def main():
    bssid = input("Enter BSSID: ").strip().lower()
    print("Scanning nearby networks...")
    networks = get_visible_networks()
    ssid = networks.get(bssid)
    if not ssid:
        print("BSSID not found or out of range.")
        sys.exit(1)
    password = get_saved_password(ssid)
    print(password if password else "NOT FOUND")

if __name__ == "__main__":
    main()
