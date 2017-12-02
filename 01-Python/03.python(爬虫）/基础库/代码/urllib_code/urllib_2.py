#-*-coding:utf-8-*-
import urllib.request
# 构建Request
request=urllib.request.Request('http://www.ibeifeng.com')
response=urllib.request.urlopen(request)
print(response.read().decode('gbk'))

