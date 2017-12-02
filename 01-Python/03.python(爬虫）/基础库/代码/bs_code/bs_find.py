from bs4 import BeautifulSoup
import codecs
soup=BeautifulSoup(codecs.open('demo1.xml',encoding='utf-8'),'html.parser')
# 获取所有的div节点
#find_all(name,attrs,rescusive,text,**kwagrs)
# name 节点名字
# attr属性
print(soup.find_all(name='p',attrs={'name':2}))

#直接传入id，来定位节点
print(soup.find_all(id='p1'))

# 查找包含www开头的链接的节点
import re
print(soup.find_all(href=re.compile('www.*')))

# 限定查找个数
print(soup.find_all(href=re.compile('www.*'),limit=1))

# rescurive 参数，默认find_all会搜索所有的子孙节点，
#rescurive设置为false，等到就是直接子节点


# //*[@id="head"]/div/div[3]  xpath
# #head > div > div.s_form    selector
#
soup.find(id='head').div.div.next_sibling.next_siblings