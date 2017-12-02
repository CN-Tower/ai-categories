#coding:utf-8
import pymysql
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']#设置默认字体
plt.rcParams['axes.unicode_minus']=False #解决保存图像时符号
# 子图
#一个figure中可以包含多个子图（axes）
#plt.subplot(numRows,numCols,plotnum)
#numRows 行数
#numCols 列数
#plotnum 指定创建的Axes对象所在的区域（从左到下的编号）
#1.数据库链接，查询数据内容，数据分列
conn=pymysql.connect(host='localhost',user='root',passwd='root',db='zp',charset='utf8')
cursor=conn.cursor()
#(1)查询城市和职位数的关系
sql1="""select zp_dd.dd_name,count(zp_list.Id) as zw_count
from zp_list inner join zp_dd on zp_dd.Id=zp_list.dd_id
group by zp_list.dd_id order by zw_count desc limit 10"""
#(2)查询城市和最大薪资与最小薪资的关系
sql2="""select zp_dd.dd_name,avg(max_zwyx),avg(min_zwyx),
count(zp_list.Id) as zw_count from zp_list
inner join zp_dd on zp_dd.Id=zp_list.dd_id
where max_zwyx<>0 and min_zwyx<>0
group by zp_list.dd_id order by zw_count desc limit 10"""
cursor.execute(sql1)
dd_zw_count_list=cursor.fetchall()
cursor.execute(sql2)
dd_max_min_zwyx_list=cursor.fetchall()
x_list=range(1,11)#x轴的刻度范围
x_label_list=[]#x轴的刻度值
ax1_y_list=[]
ax2_max_list=[]
ax2_min_list=[]
#数据分列
for item1,item2 in zip(dd_zw_count_list,dd_max_min_zwyx_list):
    x_label_list.append(item1[0])#放入城市数据
    ax1_y_list.append(item1[1])#放入职位数
    ax2_max_list.append(item2[1])#放入平均最大薪资
    ax2_min_list.append(item2[2])#放入平均最小薪资
#2.建立子图
flg=plt.figure(1)
ax1=plt.subplot(211)
ax2=plt.subplot(212)
#3.分别在不同的子图，显示不同的图表
#plt.title(u'地点和职位数与薪资的关系图')
#(1)上图，地点和职位数的关系
plt.xticks(x_list,x_label_list)
plt.ylabel(u'职位量')
plt.sca(ax1)
ax1.plot(x_list,ax1_y_list)
#数据标签
for a,b in zip(x_list,ax1_y_list):
    ax1.text(a,b,u'%d个'%b)
#(2)下图，地点和职位最大薪资与最小薪资的关系
ax2.bar(x_list,ax2_max_list,width=0.35,align='center',color='r',alpha=0.8)
#bar 柱状图
#width柱状宽度
#align 柱状的对齐方式
#color 颜色
#alpha 透明度
#bottom 堆积图的设置参考
ax2.bar(x_list,ax2_min_list,width=0.35,align='center',color='y',alpha=0.8)
#数据标签
for a,b,c in zip(x_list,ax2_max_list,ax2_min_list):
    ax2.text(a+0.3,b+200,u'%.2f元/月'%b,ha='center')
    ax2.text(a+0.3,c+200,u'%.2f元/月'%c,ha='center')
ax2.legend([u'最大薪资',u'最小薪资'],loc='upper right')
plt.xticks(x_list,x_label_list)
plt.xlabel(u'城市')
plt.ylabel(u'薪资')
plt.sca(ax2)
plt.show()
