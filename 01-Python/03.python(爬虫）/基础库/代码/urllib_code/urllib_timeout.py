#-*-coding:utf-8-*-
from urllib import request
response=request.urlopen('http://www.ibeifeng.com',timeout=10)
print(response.read().decode('gbk'))
