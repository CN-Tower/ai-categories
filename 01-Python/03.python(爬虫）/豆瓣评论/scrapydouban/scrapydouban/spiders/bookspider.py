#!/usr/bin/python
# encoding: utf-8


"""
@author: 大圣
@contact: excelchart@sina.cn
@file: novelspider.py
@time: 2015/12/23 0023 上午 11:31
"""
from scrapy.spiders import BaseSpider
from scrapy.http import Request
from scrapy.selector import Selector
from scrapydouban.items import DoubanBookItem

class Books(BaseSpider):
    name ='DoubanBooks'
    start_urls = ['http://book.douban.com/top250']


    def parse(self,response):
        item = DoubanBookItem()
        selector=Selector(response)
        books = selector.xpath('//td[@valign="top"  and not(@width)]')
        for eachbook in books:
            title=eachbook.xpath('div[@class="pl2"]/a/text()').extract()
            title = title[0]

            title2=eachbook.xpath('div[@class="pl2"]/span/text()').extract()
            title2=title2[0] if len(title2)>0 else ''
            info =eachbook.xpath('p[@class="pl"]/text()').extract()
            info = info[0]
            rate=eachbook.xpath('div[@class="star clearfix"]/span[@class="rating_nums"]/text()').extract()
            rate= rate[0]
            hot=eachbook.xpath('div[@class="star clearfix"]/span[@class="pl"]/text()').extract()
            hot = hot[0]

            item['title']=title
            item['title2']=title2
            item['info']=info
            item['rate']=rate
            item['hot']=hot
            yield item

        nextlink=selector.xpath('//span[@class="next"]/a/@href').extract()
        if nextlink:
            nextlink=nextlink[0]
            yield Request(nextlink,callback=self.parse)


