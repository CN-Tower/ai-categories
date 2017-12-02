#-*-coding:utf-8-*-
from urllib import request
# 设置HTTP处理机制,开启日志
httpHandler=request.HTTPHandler(debuglevel=1)
# 设置HTTPS处理机制，关闭日志
httpsHandler=request.HTTPSHandler(debuglevel=0)
#构建opener
opener=request.build_opener(httpHandler,httpsHandler)
#载入opener
request.install_opener(opener)
#请求
response=request.urlopen('http://www.ibeifeng.com')
print(response)
