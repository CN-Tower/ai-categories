#!/user/bin/python
#-*- coding:utf-8 -*-

'''
@author: 创客▪榕
@contact: chentianhao0510@126.com
@file: mysqlpipelines.py
@time: 2017/5/16 16:52
'''

import pymysql

class MySQLDoubanBookPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='123.20711.209', port=3306, user='root',passwd='FanTan879', db='doubanbook', charset='utf8')
        self.conn.autocommit(True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = 'insert into doubanBook (name, url, pub, rate, intr, reviews) values (%s, %s, %s, %s, %s, %s)'
        bookInfo = (item['title'], item['url'], item['pub'], item['rate'], item['intr'], item['reviews'])
        self.cursor.execute(sql,bookInfo)
        return item

    def close_db(self):
        self.conn.commit()  # 据范老师，虽然第16行有自动提交，但是这里还是加一句提交比较好
        self.cursor.close()
        self.conn.close()


