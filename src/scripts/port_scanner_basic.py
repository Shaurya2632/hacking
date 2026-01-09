import socket

ipAddress = "192.168.0.1"
minPort = 5000
maxPort = 5010

print(f"Scanning {ipAddress}")

for port in range(minPort, maxPort+1):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(.5)

        if s.connect_ex((ipAddress, port)) == 0:
            print(f'Port {port} is open')

        else:
            print(f'Port {port} is closed')

