#!/usr/bin/python
# encoding: utf-8


"""
@author: 大圣
@contact: excelchart@sina.cn
@file: bookspider2.py
@time: 2015/12/23 0023 下午 6:38
"""


from scrapy.spiders import BaseSpider
from scrapy.http import Request
from scrapy.selector import Selector
from scrapydouban.items import DoubanBookDetailItem
from urlparse import urljoin
from scrapy.utils.response import get_base_url

class Books(BaseSpider):
    name ='DoubanBooksDetail'
    start_urls = ['http://book.douban.com/top250']

    def parse(self,response):
        selector=Selector(response)
        books = selector.xpath('//td[@valign="top"  and not(@width)]')
        for eachbook in books:
            title=eachbook.xpath('div[@class="pl2"]/a/text()').extract()[0]
            href = eachbook.xpath('div[@class="pl2"]/a/@href').extract()[0]
            title2=eachbook.xpath('div[@class="pl2"]/span/text()').extract()
            title2=title2[0] if len(title2)>0 else ''
            info =eachbook.xpath('p[@class="pl"]/text()').extract()[0]
            rate=eachbook.xpath('div[@class="star clearfix"]/span[@class="rating_nums"]/text()').extract()[0]
            hot=eachbook.xpath('div[@class="star clearfix"]/span[@class="pl"]/text()').extract()[0]

            item = DoubanBookDetailItem()
            item['title']=title
            item['title2']=title2
            item['info']=info
            item['rate']=rate
            item['hot']=hot
            item['href'] = href
            item['intr'] = ''
            item['reviews']=[]

            yield Request(url=href,meta={'book':item},callback=self.parse_bookdetail)
                # print item
        nextlink=selector.xpath('//span[@class="next"]/a/@href').extract()
        if nextlink:
            nextlink=nextlink[0]
            yield Request(nextlink,callback=self.parse)

    def parse_bookdetail(self,response):
        selector=Selector(response)
        intrp = selector.xpath('//div[@class="related_info"]/div[@id="link-report"]/div/div[@class="intro"]/p/text()').extract()
        if len(intrp)>0:
            item=response.meta['book']
            intr='\r\n'.join(intrp)
            item['intr']=intr.lstrip().rstrip()
            # yield item

            # print response.url.split('/')[-2]
            baseurl=get_base_url(response)
            reviewurl=urljoin(baseurl,'reviews')
            # print reviewurl
            yield Request(url=reviewurl,meta={'book':item},callback=self.parse_bookreview)

    def parse_bookreview(self,response):
        item = response.meta['book']
        selector=Selector(response)
        reviews=selector.xpath('//div[@id="content"]/div[@class="grid-16-8 clearfix"]/div[@class="article"]/div[@class="ctsh"]/div[@class="tlst"]/div[@class="nlst"]/h3/a[@title]/@href').extract()
        if reviews:
            item['reviews'].extend(reviews)
        nextlink=selector.xpath('//span[@class="next"]/a/@href').extract()
        if nextlink:
            nextlink=response.url+nextlink[0]
            yield Request(url=nextlink,callback=self.parse_bookreview,meta={'book':item})
        else :
            yield item


