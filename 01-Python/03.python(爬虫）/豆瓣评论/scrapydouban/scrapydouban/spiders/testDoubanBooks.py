# #!/user/bin/python
# #-*- coding:utf-8 -*-
#
# '''
# @author: 创客▪榕
# @contact: chentianhao0510@126.com
# @file: testDoubanBooks.py
# @time: 2017/5/16 9:28
# '''
#
# # 本段程序用于测试scrapyDouban中的DoubanBooks是否能正常运行，如出现错误加以调试
# from lxml import etree
# import requests
#
# def getBookList():
#     oneBookUrl = u'https://book.douban.com/tag/小说?start=0&type=T'.encode('utf-8')
#     response = requests.get(oneBookUrl)
#     content = response.text
#     selector = etree.HTML(content)
#     books = selector.xpath('//li[@class="subject-item"]')
#     if books:
#         for eachbook in books:
#             bookname = eachbook.xpath('div[@class="info"]/h2/a/text()')
#             title = bookname[0]
#             bookurl = eachbook.xpath('div[@class="info"]/h2/a/@href')
#             url = bookurl[0]
#             bookpub = eachbook.xpath('div[@class="info"]/div[@class="pub"]/text()')
#             pub = bookpub[0] if bookpub else None
#             bookrate = eachbook.xpath('div[@class="info"]/div[@class="star clearfix"]/span[@class="rating_nums"]/text()')
#             rate = bookrate[0] if bookrate else None
#             yield title, url, pub, rate
#
# if __name__ == '__main__':
#     for title, url, pub, rate in getBookList():
#         print title
#         print url
#         print pub
#         print rate
#
