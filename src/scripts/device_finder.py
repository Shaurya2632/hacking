import psutil, socket, nmap, ipaddress
from mac_vendor_lookup import MacLookup

for n, a in psutil.net_if_addrs().items():
    if psutil.net_if_stats()[n].isup:
        for i in a:
            if i.family == socket.AF_INET and not i.address.startswith("127."):
                ip = i.address

net = str(ipaddress.IPv4Network(ip.rsplit(".", 1)[0] + ".0/24"))
nm = nmap.PortScanner()
nm.scan(hosts=net, arguments='-sn -PR')

for h in nm.all_hosts():
    mac = nm[h]['addresses'].get('mac', 'Unknown')
    name = next((x['name'] for x in nm[h]['hostnames'] if x['name']), socket.getfqdn(h))
    vendor = 'Unknown'
    if mac != 'Unknown':
        try: vendor = MacLookup().lookup(mac)
        except: pass
    print(f"{h:16} {mac:20} {name:25} {vendor}")
