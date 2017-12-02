#coding:utf-8
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pymysql
#福利信息词云
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
conn=pymysql.connect(host='localhost',user='root',passwd='root',db='zp',charset='utf8')
cursor=conn.cursor()
sql='select flxx_name from zp_flxx'
cursor.execute(sql)
flxx_list=cursor.fetchall()
flxx_name_list=[item[0] for item in flxx_list] #列表推导式
#将列表转换为字符串
# reduce(lambda x,y:x+' '+y,flxx_name_list)
flxx_text=' '.join(flxx_name_list)
import numpy as np
import PIL.Image as Image
import os #系统模块
#获取当前文件路径
#__file__ 表示当前文件
d=os.path.dirname(__file__)
img_mask=np.array(Image.open(os.path.join(d,'1.jpg')))
#列表中的每一项使用引号内的内容进行分割，完成拼接
#1.为了解决中文乱码问题，我们需要加上如下的操作
font='C:\Windows\Fonts\simkai.ttf'
#实例化词云对象，使用generate载入文本
#mask 图片模板
my_wordclound=WordCloud(background_color='#ffffff',font_path=font,max_font_size=300,mask=img_mask).generate(flxx_text)
plt.imshow(my_wordclound)
plt.axis('off')
plt.show()
