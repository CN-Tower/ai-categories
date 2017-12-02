#coding:utf-8
#地点和最大薪资与最小薪资关系
import pymysql
import matplotlib.pyplot as plt
#处理中文乱码
plt.rcParams['font.sans-serif']=['SimHei']#设置默认字体
plt.rcParams['axes.unicode_minus']=False #解决保存图像时符号
#连接数据库，数据查询，数据分列
#地点名称，最大薪资，最小薪资，Top10（最大薪资），where去除最大和最小薪资为0的可能
conn=pymysql.connect(host='localhost',user='root',passwd='root',db='zp',charset='utf8')
corsor=conn.cursor()
sql="""select zp_dd.dd_name,avg(max_zwyx) as max_zwyx_num,
avg(min_zwyx) as min_zwyx_num,
count(zp_list.id) as zw_count
from zp_list INNER JOIN zp_dd on zp_dd.Id=zp_list.dd_id
where max_zwyx!=0 and min_zwyx!=0
GROUP by zp_list.dd_id
order by zw_count DESC
limit 10;"""
corsor.execute(sql)
dd_xz_list=corsor.fetchall()
x_lable_list=[]#x轴刻度名称
x_list=range(1,11)#x轴刻度值
y_max_list=[]
y_min_list=[]
#数据分列
for item in dd_xz_list:
    x_lable_list.append(item[0])
    y_max_list.append(item[1])
    y_min_list.append(item[2])
#设置x轴的刻度
plt.xticks(x_list,x_lable_list)
#生成折线图
plt.plot(x_list,y_max_list,color='g')
plt.plot(x_list,y_min_list,color='y')
#标识类别
plt.legend([u'最大薪资',u'最小薪资'],loc='upper right')
#plt.legend(类别的列表,loc表示标签显示的位置)
#upper 顶部，center 居中，bottom底部
#left 左边，center 居中，right 右边
#数据标签设置
for a,b,c in zip(x_list,y_max_list,y_min_list):
    plt.text(a,b+20,u'%.2f元/月'%b)
    plt.text(a,c-20,u'%.2f元/月'%c)

#标题设置
plt.title(u'Top10城市最大薪资和最小薪资折线图')
plt.xlabel(u'城市')
plt.ylabel(u'元/月')
plt.show()
