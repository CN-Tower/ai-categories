#-*-coding:utf-8-*-
import urllib.request
import urllib.parse
import http.cookiejar
#定义文件
filename='cookie.txt'
# 申明CookieJar对象
cookie = http.cookiejar.MozillaCookieJar(filename)
# hanler 来构建opener
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
#建立数据包
values={}
values['username']='fanfzj'
values['password']='FanTan879'
values['lt']='LT-512088-b2c34SgDBOyOCU9b7sKWkC1E86aoT'
values['execution']='e2s1'
values['_eventId']='submit'
postdata=urllib.parse.urlencode(values).encode('utf-8')
url='https://passport.csdn.net/account/login'
# 模拟登录，并把cookie保存到变量
req = urllib.request.Request(url,postdata)
result=opener.open(req)
#保存cookie到cookie.txt中
cookie.save(ignore_discard=True,ignore_expires=True)
#请求登录后的一些页面
geturl='http://msg.csdn.net/letters'
reponse=opener.open(geturl)
print(reponse.read().decode('utf-8'))
