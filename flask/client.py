import requests
import socket

ip_address = "" #Change here
port = 80


try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        s.connect((ip_address, port))
        response = requests.get('http://{ip}'.format(ip=ip_address))

        if response.status_code == 200:
            output = response.json()['output']
            print(output)
        else:
            print(f"Error: {response.status_code} - {response.reason}")
except (socket.timeout, ConnectionRefusedError):
    print(ip_address, "is not reachable on port", port)
