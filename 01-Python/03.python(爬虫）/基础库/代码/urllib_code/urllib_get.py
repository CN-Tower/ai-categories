#-*-coding:utf-8-*-
import urllib.request as url_re
url='http://www.baidu.com/s?wd=ai'
request=url_re.Request(url)
response=url_re.urlopen(request)
print(response.read().decode('utf-8'))
