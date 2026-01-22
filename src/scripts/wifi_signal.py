from pywifi import PyWiFi
import time
import os

wifi = PyWiFi()
iface = wifi.interfaces()[0]

while True:
    iface.scan()
    time.sleep(0.5)     

    results = iface.scan_results()

    if results:
        os.system("cls") 
        print(f"{'SSID':30} {'Signal(dBm)':>12} {'BSSID':>20}")
        print("-" * 65)

        for network in results:
            print(f"{network.ssid:30} {network.signal:>12} {network.bssid:>20}")
    else:
        print("No networks found")
