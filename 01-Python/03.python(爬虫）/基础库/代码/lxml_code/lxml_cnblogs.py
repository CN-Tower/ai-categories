from lxml import etree
import requests
def get_list(go_url='https://www.cnblogs.com/'):
    html=requests.get(go_url).text
    sel=etree.HTML(html) #解析html源代码
    #获取文章详细页面链接，xpath返回的结果都是列表
    href=sel.xpath('//*[@id="post_list"]/div/div/h3/a/@href')
    #//*[@id="post_list"]/div[1]/div[2]/h3/a
    #获取下一页链接
    next_page=sel.xpath('//*[@id="paging_block"]/div/a[last()]')
    #//*[@id="paging_block"]/div/a[13]
    #//*[@id="pager_top"]/div/a[8]
    return href,next_page

#访问文章详细信息，获取文章的详细内容，存储到一个列表里
def get_info(url,save_list):
    html = requests.get(url).text
    sel = etree.HTML(html)
    title=sel.xpath('//*[@id="cb_post_title_url"]/text()')
    if title:
        title=title[0]
    else:
        print(url)
        return '',''
    #text只能获取当前标签的文本，不能获取他子孙标签的文本
    content=sel.xpath('string(//*[@id="cnblogs_post_body"])')
    # 假如使用了string，那么xpath方法返回的结果，就不是一个列表，而是一个字符串
    save_dict={}
    save_dict['title']=title
    save_dict['content']=content
    save_list.append(save_dict)

urls_list=[]
urls, next_url = get_list()
urls_list.extend(urls)
while True:
    if next_url:
        if next_url[0].xpath('text()')[0]=='Next >':
            urls, next_url=get_list('http://www.cnblogs.com'+next_url[0].xpath('@href')[0])
            print('http://www.cnblogs.com'+next_url[0].xpath('@href')[0])
            urls_list.extend(urls)
        else:
            break
    else:
        break
save_list=[]
for url in urls_list:
    get_info(url,save_list)

import pandas as pd
save = pd.DataFrame(save_list)
print(save)
save.to_csv('b.csv',index=False,sep='')


# 访问首页-> 详细页面链接获取的函数（返回一个链接列表）->循环列表，依次将链接-》详细页面数据抓取的函数（返回一个文章名和文章内容）-》数据存储