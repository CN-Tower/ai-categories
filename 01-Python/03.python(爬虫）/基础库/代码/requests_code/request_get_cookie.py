import requests
url = 'http://www.ibeifeng.com'
r = requests.get(url)
print(r.cookies)
print(r.cookies['ECS[visit_times]'])