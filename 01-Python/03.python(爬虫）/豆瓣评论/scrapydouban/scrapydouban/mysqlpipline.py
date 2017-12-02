#!/usr/bin/python
# encoding: utf-8


"""
@author: 大圣
@contact: excelchart@sina.cn
@file: mysqlpipline.py
@time: 2015/12/24 0024 下午 9:06
"""


import MySQLdb

class MySQLDoubanBookPipline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(host='localhost',port=3306,user='root',
                           passwd='root',db='testdb',charset='utf8')
        self.conn.autocommit(True)
        self.cursor = self.conn.cursor()

    def process_item(self,item,spider):
        sql='insert into doubanbook(title,title2,rate,hot,intr,info) values (%s,%s,%s,%s,%s,%s)'
        bookinfo=[item['title'],item['title2'],item['rate'],item['hot'],item['intr'],item['info']]
        self.cursor.execute(sql,bookinfo)
        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()
