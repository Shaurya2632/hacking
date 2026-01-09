from pywifi import PyWiFi

wifi = PyWiFi()
iface = wifi.interfaces()[0]
iface.scan()

results = iface.scan_results()

print(f"{'SSID':30} {'Signal(dBm)':>12} {'BSSID':>20}")
print("-" * 65)

for network in results:
    print(f"{network.ssid:30} {network.signal:>12} {network.bssid:>20}")