# # -*- coding: utf-8 -*-
#
# from scrapy.spiders import BaseSpider
# from scrapy.http import Request
# from scrapy.selector import Selector
# import sys
# sys.path.append('C:\\Users\\cuihao\\Desktop\\python(dasheng)\\myProject\\scrapyDouban\\scrapyDouban')
# from items import DoubanBookItem  # 该名字一定要和items里面的类名相同
# # 第6,7,8三行import DoubanBookItem的方法，大圣老师的的方法行不通，必须使用以上方法，如果换电脑，记得修改append后面的路径！！！
#
# class Books(BaseSpider):
#     name = 'DoubanBooks'  # name一定要和main里面的相同！！！
#     start_urls = [u'https://book.douban.com/tag/小说'.encode('utf-8')]
#
#     def parse(self, response):
#         item = DoubanBookItem()
#         selector = Selector(response)
#         books = selector.xpath('//li[@class="subject-item"]')
#         if books:
#             for eachbook in books:
#                 bookname = eachbook.xpath('div[@class="info"]/h2/a/text()').extract()
#                 title = bookname[0]
#                 bookurl = eachbook.xpath('div[@class="info"]/h2/a/@href').extract()
#                 url = bookurl[0]
#                 bookpub = eachbook.xpath('div[@class="info"]/div[@class="pub"]/text()').extract()
#                 pub = bookpub[0] if bookpub else None
#                 bookrate = eachbook.xpath('div[@class="info"]/div[@class="star clearfix"]/span[@class="rating_nums"]/text()').extract()
#                 rate = bookrate[0] if bookrate else None
#
#                 item['title'] = title
#                 item['url'] = url
#                 item['pub'] = pub
#                 item['rate'] = rate
#                 yield item
#                 # 一定要注意，item只是一个变量，其类型是dict,用来存储书籍信息的，以上4个赋值是给字典的每个key赋值
#         nextlink = selector.xpath('//div[@class="paginator"]/span[@class="next"]/a/@href').extract()[0]
#         if nextlink:
#             nextlink = "https://book.douban.com" + nextlink  # 注意这种拼接url的方式，此处拼接不对就无法获取其他页面
#             yield Request(nextlink, callback=self.parse)
#
#
#
#
#
#
#
#
#
