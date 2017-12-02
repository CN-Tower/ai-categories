#-*-coding:utf-8-*-
import urllib.request as url_re
import urllib.parse as url_pa
url='http://123.207.11.209/ajax.php'
# 建立数据包
post_data={'username':'admin','password':'123456'}
data=url_pa.urlencode(post_data)
# 建立url请求
request=url_re.Request(url)
# data数据必须是字节型字符串
response=url_re.urlopen(request,data.encode('utf-8'))
print(response.read().decode('utf-8'))

