#coding:utf-8
#公司规模的饼图
import pymysql
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']#设置默认字体
plt.rcParams['axes.unicode_minus']=False #解决保存图像时符号
#连接数据库，计算每个公司规模分类所占的比例
conn=pymysql.connect(host='localhost',user='root',passwd='root',db='zp',charset='utf8')
cursor=conn.cursor()#相当于链接一个mysql -uroot -p的mysql的窗口，mysql会话
sql="""select zp_gsgm.gsgm_name,count(*)/(select count(*) from zp_list) from 
zp_list INNER join zp_gsgm on zp_gsgm.Id=zp_list.gsgm_id
group by zp_list.gsgm_id"""
cursor.execute(sql)
gsgm_list=cursor.fetchall()
label_list=[]#标签
sizes_list=[]#所占的比例
for item in gsgm_list:
    label_list.append(item[0]+' '+str(round(item[1]*100,2))+'%')
    sizes_list.append(item[1])
#设置绘图区域的大小
axes=plt.subplots(figsize=(10,6),ncols=2)#绘图区域，左右分割，左边占10个空间，右边占6个空间
# #提取左右绘图区
ax1,ax2=axes[1]#维度拉伸,numpy中方法(拉伸)
#[[1 2],[3 4]] ravel=> [1 2 3 4]
ax1.set_title(u'公司规模与职位数的关系图')
ax1.axis('equal')
#startangle 开始的角度
pa,texts=ax1.pie(sizes_list,labels=None,startangle=0)
ax2.axis('off')
ax2.legend(pa,label_list,loc='center right')
plt.show()