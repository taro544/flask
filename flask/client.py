import requests

response = requests.get('http://localhost:80')

if response.status_code == 200:
    output = response.json()['output']
    print(output)
else:
    print(f"Error: {response.status_code} - {response.reason}")
