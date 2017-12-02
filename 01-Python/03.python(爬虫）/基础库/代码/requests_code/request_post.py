import requests
payload = {'key1': 'value1', 'key2': 'value2'}
#post请求
r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)
