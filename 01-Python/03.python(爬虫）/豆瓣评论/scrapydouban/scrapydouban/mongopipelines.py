#!/user/bin/python
#-*- coding:utf-8 -*-

'''
@author: 创客▪榕
@contact: chentianhao0510@126.com
@file: mongopipelines.py
@time: 2017/5/16 16:51
'''

from scrapy.conf import settings
from pymongo import MongoClient

class MongoDoubanBookPipeline(object):
    def __init__(self):
        dbserver = settings['MONGODB_SERVER']
        dbport = settings['MONGODB_PORT']
        dbname = settings['MONGODB_DB']
        colname = settings['MONGODB_COLLECTION']
        client = MongoClient(dbserver, dbport)
        db = client[dbname]
        self.col = db[colname]
        # 注意以上的括号，有的是中括号，有的是小括号，我没有搞清楚这其中的究竟，但是一定要记住括号不能写错！！！

    def process_item(self, item, spider):
        book = dict(item)
        self.col.insert(book)
        return item  # 我没有搞懂为什么要用这句，应该是模板默认设置如此,就好比parce,process第二个之后必须用下划线一样

    def close_spider(self, spider):
        pass



