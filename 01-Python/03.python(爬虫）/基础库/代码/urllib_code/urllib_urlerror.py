#-*-coding:utf-8-*-
from urllib import request
req=request.Request('http://www.ibeifeng1.com')
try:
    print(request.urlopen(req).read().decode('gbk'))
except error.URLError as e:
    print(e.reason)
else:
    print('ok')
