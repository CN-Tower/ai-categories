#-*-coding:utf-8-*-
import urllib.request
# 传入一个链接，协议是HTTP协议
# urllib.request.urlopen(url,data,timeout)
# url URL链接，网址
# data 访问url时候发送的数据包，默认weiNone
# timeout 设置超市，默认socket._GLOBAL_DEFAULT_TIMEOUT
# 返回一个response 对象
response=urllib.request.urlopen('http://www.ibeifeng.com')
# read() 读取网页的源代码,返回字节对象
print(response)
