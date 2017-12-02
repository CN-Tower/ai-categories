from bs4 import BeautifulSoup
import requests
html=requests.get('http://www.baidu.com').text
soup=BeautifulSoup(html,'html.parser')
print(soup)
print(type(soup))