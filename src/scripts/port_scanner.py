import re
import nmap
import pyfiglet

ipAddressPattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
portRangePattern = re.compile("([0-9]+)-([0-9]+)")

portMin = 0
portMax = 65535

pyfiglet.print_figlet("PortScanner", "Slant")

openPorts = []

while True:
    userIpAddress= input("\nEnter ip address to scan: ")

    if ipAddressPattern.search(userIpAddress):
        print(f"{userIpAddress} is valid")
        break

while True:
    portRange =  portRangePattern.search(input("Enter port range (min-max): ").replace(" ", ""))
    if portRange:
        portMin = int(portRange.group(1))
        portMax = int(portRange.group(2))
        break

scanner = nmap.PortScanner()

for port in range(portMin, portMax + 1):
    try:
        result = scanner.scan(userIpAddress, str(port))
        status = (result['scan'][userIpAddress]['tcp'][port]['state'])

        print(f"Port {port} is {status}")

    except:
        print(f"Can't scan port {port}")
