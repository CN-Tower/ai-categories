#-*-coding:utf-8-*-
import urllib.request
import http.cookiejar
# 申明CookieJar对象
cj = http.cookiejar.CookieJar()
# 构建cookie处理
hanler = urllib.request.HTTPCookieProcessor(cj)
# hanler 来构建opener
opener=urllib.request.build_opener(hanler)
urllib.request.install_opener(opener)
# open方法传入url
response=opener.open('http://www.ibeifeng.com')
for item in cj:
    print('Name:'+item.name)
    print('Value:' + item.value)
