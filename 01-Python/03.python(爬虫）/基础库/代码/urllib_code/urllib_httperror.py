#-*-coding:utf-8-*-
from urllib import request,error
req=request.Request('http://www.douyu.com/Jack_Cui.html')
try:
    print(request.urlopen(req).read())
except error.HTTPError as e:
    print(e.reason)
    print(e.code)
except error.URLError as e:
    print(e.reason)
else:
    print('ok')
