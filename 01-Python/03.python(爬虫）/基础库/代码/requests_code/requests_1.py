import requests
r = requests.get('http://www.ibeifeng.com')
print(type(r))
print(r.status_code)
print(r.encoding)
print(r.cookies)