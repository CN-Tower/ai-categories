# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DdwebItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    good_id=scrapy.Field()
    good_title=scrapy.Field()
    good_cat=scrapy.Field()
    good_price=scrapy.Field()
