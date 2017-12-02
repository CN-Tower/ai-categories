import requests
r = requests.get("https://github.com/timeline.json", stream=True)
print(r.text)#网页源码
print(r.json())#json解析
print(r.raw) #获取套接字