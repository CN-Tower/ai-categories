#-*-coding:utf-8
import time

# 1. 返回当前时间戳
t = time.time()
print ("Current time:", t)

# 2. 将时间戳转换为当前时区下的时间元组
tup1 = time.localtime(t)
print (tup1)
print (u"年份:", tup1.tm_year)
print (u"月份:", tup1.tm_mon)
print (u"日期:", tup1.tm_mday)
print()
#tm_year  年
#tm_mon 月
#tm_mday  日
#tm_hour 时
#tm_min  分
#tm_sec  秒
#tm_wday  一周的第几天（0-6）
#tm_yday  一年中第几天（1-366）
#tm_isdst  是否是夏令时区

# 3. 将时间元组转换为时间戳(毫秒会忽略)
print ("Current time is:", time.mktime(tup1))
print ()

# 4.0. 获取CPU运行时间来获取比较精确的运行秒数，一般用于时间间隔的获取/比较
# 4.1. 休眠/停止一段时间， 指定需要停止的秒数
print (u"开始时间:", time.clock())
time.sleep(5)
print (u"结束时间1:", time.clock())
time.sleep(5)
print (u"结束时间2:", time.clock())
print()

# 5. 格式化时间元组给给定字符串
tm_str = time.strftime("%Y-%m-%d %H:%M:%S", tup1)
print (u"格式化时间:", tm_str)
#%Y  四位数年份    %y 两位数年份
#%m  月份          %M 分钟   ***
#%d  一个月内的第几天
#%H  24进制的时间  %I  12进制时间
#%S  秒数
#%a  本地简化星期    #%A 完整日期
#%b  本地简化月份    #%B 完整月份
#%c  相应日期和时间
#%j   一年中的第几天   %p  pm与am标识
#%U   当前星期是一年中的第几个（1-54）
#%W    当前星期是一年中第几个（0-53）
#%w   星期几（整型）（从周日开始）（0-6）
#%x    本地相应日期标识  %X    本地相应时间标识
#%Z    时区

# 6. 格式化时间字符串成为时间元组
tup2 = time.strptime(tm_str, "%Y-%m-%d %H:%M:%S")
print (tup2)
