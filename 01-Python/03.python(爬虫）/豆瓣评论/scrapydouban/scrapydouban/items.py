# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field
# 注意，item是字典类型，所以在parse中赋值的时候类似于字典赋值

class DoubanBookItem(Item):
    title = Field()
    url = Field()
    pub = Field()
    rate = Field()

class DoubanBookDetailItem(Item):
    title = Field()
    url = Field()
    pub = Field()
    rate = Field()
    intr = Field()    # 本书的摘要
    reviews = Field()  # 本书所有评论的url列表
    title2=Field()
    info=Field()
    hot=Field()
    href=Field()


