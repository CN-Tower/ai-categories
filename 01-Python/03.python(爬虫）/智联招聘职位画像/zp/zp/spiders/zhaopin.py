# -*- coding: utf-8 -*-
import scrapy
import re
import json
from zp.zp_items import ZpItem

class ZhaopinSpider(scrapy.Spider):
    name = 'zhaopin'  #爬虫名
    allowed_domains = ['zhaopin.com']  #允许访问的域名
    start_urls = ['http://sou.zhaopin.com/']  #进口链接

    #职位类别列表
    def parse(self, response):
        sel=scrapy.Selector(response)
        a_list=sel.xpath('//div[@id="search_right_demo"]/div/div[@class="clearfixed"]/a')
        for a_item in a_list:
            url=self.start_urls[0]+a_item.xpath('@href').extract()[0]
            #489表示全国，通过手动修改链接控制抓取全部城市知新信息
            url=url[:url.find('=')+1]+'489'+url[url.find('&'):]
            yield scrapy.Request(url=url,callback=self.parse_list,dont_filter=True)

    #通过列表页面获取详细页面链接，并完成分页处理
    def parse_list(self,response):
        #1.建立选择器
        selector=scrapy.Selector(response)
        #2.完成列表详细页面链接的获取
        table_a_xpath=selector.xpath('//*[@id="newlist_list_content_table"]/table/tr[1]/td[1]/div/a/@href').extract()
        for url in table_a_xpath:
            #循环取出每一条链接，然后提交后续处理方法
            yield scrapy.Request(url=url,callback=self.parse_info)
        #3.完成下一页处理
        next_page=selector.xpath('//a[@class="next-page"]/@href').extract()
        #判断下一页链接是否存在
        if next_page:
            #将下一页的数据，传递给自身
            yield scrapy.Request(url=next_page[0],callback=self.parse_list)


    #4.完成详细页面数据获取
    def parse_info(self,response):
        sel=scrapy.Selector(response)
        #1.职位名称
        zwmc=sel.xpath('//div[@class="top-fixed-box"]/div[@class="fixed-inner-box"]/div[1]/h1/text()').extract()
        #2.公司名称
        gsmc = sel.xpath('//div[@class="top-fixed-box"]/div[@class="fixed-inner-box"]/div[1]/h2/a/text()').extract()
        #3.福利信息
        flxx=sel.xpath('//div[@class="top-fixed-box"]/div[@class="fixed-inner-box"]/div[1]/div/span/text()').extract()

        #获取ul下的li的span和strong
        ul_li = sel.xpath('//ul[@class="terminal-ul clearfix"]/li')
        info_dict = {}
        for item in ul_li:
            #decode 解码为unicode
            span_one=unicode(item.xpath('span/text()').extract()[0].strip(u"："))
            #string 表示获取strong下的所有文本，不管下面的节点包含关系
            #会有缺点，他会保留所有的空格
            strong_one = item.xpath('string(strong)').extract()[0]
            #对strong_one的文本中的空格进行处理
            strong_list=[one.strip() for one in strong_one.split()]
            strong_one=''.join(strong_list)
            info_dict[span_one]=strong_one
        ul_li = sel.xpath('//ul[@class="terminal-ul clearfix terminal-company mt20"]/li')
        for item in ul_li:
            # decode 解码为unicode
            span_one = unicode(item.xpath('span/text()').extract()[0].strip(u"："))
            # string 表示获取strong下的所有文本，不管下面的节点包含关系
            # 会有缺点，他会保留所有的空格
            strong_one = item.xpath('string(strong)').extract()[0]
            # 对strong_one的文本中的空格进行处理
            strong_list = [one.strip() for one in strong_one.split()]
            strong_one = ''.join(strong_list)
            info_dict[span_one] = strong_one
        #4.职位月薪
        zwyx=info_dict.get(u'职位月薪','').strip(u'元/月')
        if zwyx==u'面议':
            zwyx=''
        #分割月薪数据
        zwyx_list=zwyx.split('-')
        #判断是否分割成两部分了，如果可以，则最低和最高分别赋值给两个变量，如果不可以，则最低和最高赋值为zwyx的值
        if len(zwyx_list)==2:
            min_zwyx=zwyx_list[0]
            max_zwyx=zwyx_list[1]
        else:
            min_zwyx=max_zwyx = zwyx
        #5.工作地点

        gzdd=info_dict.get(u'工作地点','')
        #6.发布时间
        fbrq=info_dict.get(u'发布日期','')
        #7.公司性质
        gsxz=info_dict.get(u'公司性质', '')
        #8.工作经验
        gzjy=info_dict.get(u'工作经验', '')
        #9.最低学历
        zdxl=info_dict.get(u'最低学历', '')
        #10.招聘人数
        zprs=info_dict.get(u'招聘人数', '').strip(u'人')
        #11.职位类别
        zwlb=info_dict.get(u'职位类别', '')
        #12.公司规模
        gsgm=info_dict.get(u'公司规模', '')

        #13.公司行业
        gshy=info_dict.get(u'公司行业', '')
        #**14.公司主页、公司地点 。。。。。
        #获取岗位职责和任职要求
        text_xpath = sel.xpath('string(//div[@class="tab-inner-cont"][1])').extract()
        #提取岗位职责和任职要求
        #使用正则表达式
        com=re.compile(u'(要求|职责)[：:]?(.*?)(任职要求|职位描述|工作职责)[：:](.*?)工作地址：',re.S)
        re_list=re.findall(com,unicode(text_xpath[0]))
        #岗位职责和任职要求
        if re_list:
            gwzz=re_list[0][1].strip()
            rzyq=re_list[0][3].strip()
        else:
            com = re.compile(u'(.*?)工作地址：', re.S)
            re_list = re.findall(com, unicode(text_xpath[0]))
            if re_list:
                rzyq=re_list[0].strip()
            else:
                rzyq=''
            gwzz=''
        item_one=ZpItem()
        item_one['zwmc']=zwmc[0]
        item_one['gsmc'] = gsmc[0]
        item_one['flxx'] = flxx
        item_one['min_zwyx'] = min_zwyx
        item_one['max_zwyx'] = max_zwyx
        item_one['gzdd'] = gzdd
        item_one['fbrq'] = fbrq
        item_one['gsxz'] = gsxz
        item_one['gzjy'] = gzjy
        item_one['zdxl'] = zdxl
        item_one['zprs'] = zprs
        item_one['zwlb'] = zwlb
        item_one['gsgm'] = gsgm
        item_one['gshy'] = gshy
        item_one['gwzz'] = gwzz
        item_one['rzyq'] = rzyq
        item_one['href'] = response.url
        yield item_one