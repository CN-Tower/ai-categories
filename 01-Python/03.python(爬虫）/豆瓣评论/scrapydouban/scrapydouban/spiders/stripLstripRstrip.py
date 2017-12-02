# #!/user/bin/env python
# #-*- coding: utf-8 -*-
#
# '''
# @author:创客·榕
# @contact:chentianhao0510@126.com
# @file:stripLstripRstrip.py
# @time:2017/5/16 21:23
# '''
#
# # Python中的strip用于去除字符串的首尾字符，同理，lstrip用于去除左边的字符，rstrip用于去除右边的字符。
# # 这三个函数都可传入一个参数，指定要去除的首尾字符。
# # 需要注意的是，传入的是一个字符数组，编译器去除两端所有相应的字符，直到没有匹配的字符，比如：
#
# theString = 'saaaay yes no yaaaass'
# print theString.strip('say')
# # theString依次被去除首尾在['s'，'a'，'y']数组内的字符，直到字符在不数组内。所以，输出的结果为：
# # yes no
# # 比较简单吧，lstrip和rstrip原理是一样的。
# # 注意：当没有传入参数时，是默认去除首尾空格的。
#
# theString = 'saaaay yes no yaaaass'
# print theString.strip('say')
# print theString.strip('say ') #say后面有空格
# print theString.lstrip('say')
# print theString.rstrip('say')
# # 运行结果：
# #  yes no
# # es no
# #  yes no yaaaass
# # saaaay yes no
# #
