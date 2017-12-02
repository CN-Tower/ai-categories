import requests
r = requests.get('http://github.com', timeout=0.001)
print(r.text)
