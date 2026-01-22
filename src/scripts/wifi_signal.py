from pywifi import PyWiFi
import time
import os

wifi = PyWiFi()
iface = wifi.interfaces()[0]

while True:
    iface.scan()
    time.sleep(0.5)     

    networks = iface.scan_results()
    
    seen = set()
    unique_networks = [n for n in networks if n.ssid not in seen and not seen.add(n.ssid)]
    
    networks = unique_networks

    if networks:
        os.system("cls") 
        print(f"{'SSID':30} {'Signal(dBm)':>12} {'BSSID':>20}")
        print("-" * 65)

        for network in networks:
            print(f"{network.ssid:30} {network.signal:>12} {network.bssid:>20}")
    else:
        print("No networks found")
