#-*-coding:utf-8-*-
import urllib.request
import http.cookiejar
#定义文件
filename='cookie.txt'
# 申明CookieJar对象
cookie = http.cookiejar.MozillaCookieJar(filename)
# 构建cookie处理
hanler = urllib.request.HTTPCookieProcessor(cookie)
# hanler 来构建opener
opener=urllib.request.build_opener(hanler)
urllib.request.install_opener(opener)
# open方法传入url
response=opener.open('http://www.ibeifeng.com')
# 保存cookie文件
# ignore_discard，即使cookie被丢弃，是否保存
# ignore_expires，如果在该文件中cookie已存在，是否覆盖
cookie.save(ignore_discard=True,ignore_expires=True)
