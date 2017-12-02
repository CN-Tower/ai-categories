# -*- coding: utf-8 -*-
import scrapy
from ddWeb.items import DdwebItem

class DdSpider(scrapy.Spider):
    # 千万不要自定义__init__函数
    name = 'dd'   # 爬虫
    allowed_domains = ['www.dangdang.com','category.dangdang.com']  #允许的域名
    start_urls = ['http://category.dangdang.com/pg2-cid4009502.html'] #起始地址


    # 1.抓取分类列表页面链接
    # 2.抓取分类列表中详细商品链接
    # 3.商品信息抓取

    # 默认处理方法
    def parse(self, response):
    #     # 1.抓取分类列表页面链接
    #     # 如下代码类似于 sel=xtree.HTML(response.body)
    #     sel=scrapy.Selector(response)
    #     # extract 将选择器转换为列表
    #     a_list=sel.xpath('//div[@class="e"]/a/@href').extract()
    #     print(a_list)
    #     # 将链接变成一个请求发送给下载器，并且指定回调函数
    #     for url in a_list:
    #         # 等同于return的作用，但是不同于return
    #         # yield 把所有的return的结果放到一起，形成一个可迭代对象
    #         # yield 类似与水车
    #         print(url)
    #         yield scrapy.Request(url,callback=self.parse_list)
    #     # 列表推导式
    #     #return [scrapy.Request(url,callback=self.parse_list) for url in a_list]
    # # 2.抓取分类列表中详细商品链接,并且完成下一页机制
    # def parse_list(self,response):
        print(response.url)
        sel = scrapy.Selector(response)
        a_list = sel.xpath('//*[@id="component_0__0__8609"]/li/a/@href').extract()
        for url in a_list:
            #dont_filter 不做域名验证
            yield scrapy.Request(url,callback=self.parse_info,dont_filter=True)
        #下一页的处理
        next_page=sel.xpath('//li[@class="next"]/a/@href').extract()
        if next_page:#判断是否抓取到数据
            next_url="http://category.dangdang.com"+next_page[0]
            return scrapy.Request(next_url,callback=self.parse)

    # 3.商品信息抓取
    def parse_info(self,response):
        print(response.url)
        sel=scrapy.Selector(response)
        #商品信息
        #1.商品名
        good_title=sel.xpath('//div[@class="name_info"]/h1/text()').extract()
        #2.商品id
        good_id=response.url.split('/')[-1].strip('.html')
        #3.商品价格
        good_price = sel.xpath('//*[@id="dd-price"]/text()').extract()
        #4.所属分类
        good_cat=sel.xpath('string(//*[@id="detail-category-path"]/span)').extract()

        # 要通过items容器交给后面的管道进行处理
        #1.定义Items >items.py文件中操作
        #2.使用items存储数据  > 引入新的items容器

        item=DdwebItem()
        item['good_id']=good_id
        item['good_title'] = good_title[0].strip()
        item['good_price'] = good_price[0]
        item['good_cat'] = good_cat
        # 3.返回items给管道  >return item
        return item