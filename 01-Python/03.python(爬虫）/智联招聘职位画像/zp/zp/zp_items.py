# -*- coding: utf-8 -*-

import scrapy


class ZpItem(scrapy.Item):
    zwmc=scrapy.Field() #职位名称
    gsmc=scrapy.Field() #公司名称
    flxx=scrapy.Field() #福利
    min_zwyx=scrapy.Field()#最大职位月薪
    max_zwyx=scrapy.Field()#最低职位月薪
    gzdd=scrapy.Field()#工作地点
    fbrq=scrapy.Field()#发表日期
    gsxz=scrapy.Field()#公司性质
    gzjy=scrapy.Field()#工作经验
    zdxl=scrapy.Field()#最低学历
    zprs=scrapy.Field()#招聘人数
    zwlb=scrapy.Field()#职位类别
    gsgm=scrapy.Field()#公司规模
    gshy=scrapy.Field()#公司行业
    gwzz=scrapy.Field()#岗位职责
    rzyq=scrapy.Field()#任职要求
    href=scrapy.Field()#链接