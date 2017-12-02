#-*-coding:utf-8-*-
from urllib import request
req=request.Request('http://www.ibeifeng.com',method='PUT')
response=request.urlopen(req)
print(response.read().decode('gbk'))
