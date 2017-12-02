#!/usr/bin/python
# encoding: utf-8


"""
@author: 大圣
@contact: excelchart@sina.cn
@file: mongopipline.py
@time: 2015/12/24 0024 下午 9:07
"""

from scrapy.conf import settings
from  pymongo import MongoClient

class MongoDoubanBookPipline(object):
    def __init__(self):
        dbserver=settings['MONGODB_SERVER']
        dbport=settings['MONGODB_PORT']
        dbname = settings['MONGODB_DB']
        collname = settings['MONGODB_COLLECTION']
        client = MongoClient(dbserver,dbport)
        db=client[dbname]
        self.col = db[collname]

    def process_item(self,item,spider):
        book=dict(item)
        self.col.insert(book)
        return item

    def close_spider(self,spider):
        pass