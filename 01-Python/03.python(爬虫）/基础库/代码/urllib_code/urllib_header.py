#-*-coding:utf-8-*-
import urllib.request as url_re
headers={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3124.10 Safari/537.36"}
url='http://www.baidu.com/s?wd=ai'
request=url_re.Request(url,headers=headers)
response=url_re.urlopen(request)
print(response.read().decode('utf-8'))
