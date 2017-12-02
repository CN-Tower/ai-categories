#!/user/bin/env python
#-*- coding: utf-8 -*-

'''
@author:创客·榕
@contact:chentianhao0510@126.com
@file:DoubanBooks2.py
@time:2017/5/16 20:41
'''

from scrapy.spiders import BaseSpider
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.utils.response import get_base_url
from urlparse import urljoin
import sys
sys.path.append('C:\\Users\\cuihao\\Desktop\\python(dasheng)\\myProject\\scrapyDouban\\scrapyDouban')
from ..items import DoubanBookDetailItem

class BookDetails(BaseSpider):
    name = 'DoubanBooksDetail'
    start_urls = [u'https://book.douban.com/tag/小说'.encode('utf-8')]

    def parse(self, response):
        selector = Selector(response)
        books = selector.xpath('//li[@class="subject-item"]')
        if books:
            for eachbook in books:
                bookname = eachbook.xpath('div[@class="info"]/h2/a/text()').extract()
                title = bookname[0]
                bookurl = eachbook.xpath('div[@class="info"]/h2/a/@href').extract()
                url = bookurl[0]
                bookpub = eachbook.xpath('div[@class="info"]/div[@class="pub"]/text()').extract()
                pub = bookpub[0] if bookpub else None
                bookrate = eachbook.xpath(
                    'div[@class="info"]/div[@class="star clearfix"]/span[@class="rating_nums"]/text()').extract()
                rate = bookrate[0] if bookrate else None

                item = DoubanBookDetailItem()
                item['title'] = title
                item['url'] = url
                item['pub'] = pub
                item['rate'] = rate
                item['intr'] = ''
                item['reviews'] = []

                yield Request(url=url, meta={'books': item}, callback=self.parse_bookAbstract)
                # 注意，这里不是返回item，而是返回一个Request请求，Scrapy Engine会将此请求再次发出，Downloader会根据此请求继续到Internet下载所需内容
                # 三个参数的含义：url就是每本书籍的链接，callback表示回调下文的parseBookDetail这个函数，以获得书籍的摘要
                # 特别注意meta这个参数，其作用在于将item传下去，继续增加书籍信息
                # 这个yield不用进行for遍历，由于Request方法的存在，可以将相关参数直接传入parseBookAbstract中

        nextlink = selector.xpath('//div[@class="paginator"]/span[@class="next"]/a/@href').extract()[0]
        if nextlink:
            nextlink = "https://book.douban.com" + nextlink
            yield Request(nextlink, callback=self.parse)

    def parse_bookAbstract(self, response):  # 注意parce函数的名字不能乱改，第二个以后的都要用下划线的形式！！！
        selector = Selector(response)
        abstract = selector.xpath('//div[@class="indent"]/span[@class="all hidden"]/div/div[@class="intro"]/p/text()').extract()
        if abstract:  # 注意，这里大圣老师用的是if len(abstract)>0
            item = response.meta['books']
            abstract = '\r\n'.join(abstract).lstrip().rstrip()  # 注意，这里的'\r\n'要用反斜线，不能用正斜线！！！
            item['intr'] = abstract

        item = response.meta['books']
        baseUrl = get_base_url(response)  # 注意，这里的get_base_url是获得返回结果中的最基本url
        reviewUrl = urljoin(baseUrl, 'reviews')  # 将url拼接起来
        yield Request(reviewUrl, meta={'books': item}, callback=self.parse_getBookReview)

    def parse_getBookReview(self, response):
        selector = Selector(response)
        reviews = selector.xpath('//div[@class="review-list"]')
        for eachReview in reviews:
            item = response.meta['books']
            eachReviewUrl = eachReview.xpath(
                'div[@typeof="v:Review"]/div[@class="main review-item"]/div[@class="main-bd"]/div[@class="review-short"]/div[@class="short-content"]/a/@href').extract()
            if eachReviewUrl:
                item['reviews'].extend(eachReviewUrl)
            yield item

        nextPage = selector.xpath('//span[@class="next"]/a/@href').extract()
        if nextPage:
            nextPage = urljoin(get_base_url(response), nextPage[0])
            yield Request(nextPage, callback=self.parse_getBookReview, meta={'books': response.meta['books']})
            # 注意这里我第一次写的时候，想仿照没有传入item参数，这里一定要传，不能仿照第56行，因为第56行定义于第一个函数之中，这个函数是为了取前四个参数，
            # 这四个参数一次即可取完整，所以不需要再往下传参数，而这里的话，一本书的reviews还没有取完整，所以要继续往下传参数！！！
