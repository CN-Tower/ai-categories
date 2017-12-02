#-*-coding:utf-8-*-
import urllib.request
import http.cookiejar
# 申明CookieJar对象
cookie = http.cookiejar.MozillaCookieJar()
#从文件中读取cookie的内容到变量
cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True)
#创建请求的request
request=urllib.request.Request('http://www.ibeifeng.com')
# hanler 来构建opener,传入cookie
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
reponse=opener.open(request)
# open方法传入url
print(reponse.read().decode('gbk'))
