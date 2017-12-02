#coding:utf-8
#地点和职位数量的关系图表（柱状图）
import pymysql
import matplotlib.pyplot as plt #图表库

#1.链接数据库
conn=pymysql.connect(host='localhost',user='root',passwd='root',db='zp',charset='utf8')
#2.创建操作游标
cursor=conn.cursor()
#3.查询数据库
#得到Top10的城市的职位数量
#查询城市名和对应城市的职位数量，取前十条数据
sql="""select zp_dd.dd_name,count(zp_list.Id) as zw_num
from zp_list inner join zp_dd on zp_list.dd_id=zp_dd.Id
group by zp_list.dd_id order by zw_num desc limit 10;"""
cursor.execute(sql) #查询
dd_zw_num_list=cursor.fetchall()  #得到所有结果集
#print dd_zw_num_list
#数据分列
x_list=[]#x轴
x_axis_list=[]#x轴坐标名称
y_list=[]#y轴
i=1
for item in dd_zw_num_list:
    x_list.append(i)#城市名
    i+=1
    x_axis_list.append(item[0])
    y_list.append(item[1])#对应的职位数量
#处理中文乱码
plt.rcParams['font.sans-serif']=['SimHei']#设置默认字体
plt.rcParams['axes.unicode_minus']=False #解决保存图像时符号显示方块的问题
#设置坐标轴
# ax=plt.gca()
# ax.set_xticks(range(1,11)) #坐标轴范围
# ax.set_xticklabels(x_axis_list)#设置坐标轴的刻度名称
plt.xticks(x_list,x_axis_list)  #设置坐标轴的范围以及对应的刻度值
#设置数据标签
for a,b in zip(x_list,y_list):
    plt.text(a,b+1000,u'%d个'%b,ha='center')
    #plt.text(x的坐标，y的坐标，显示的内容，ha为文字横向对齐方式)
plt.plot(x_list,y_list)#折线图
plt.show()  #显示图表