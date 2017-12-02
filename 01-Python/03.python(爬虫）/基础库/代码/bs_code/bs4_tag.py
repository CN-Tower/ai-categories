from bs4 import BeautifulSoup
import codecs
soup=BeautifulSoup(codecs.open('demo1.xml',encoding='utf-8'),'html.parser')

#1.直接子节点,获取的是第一个div的节点的所有内容
# print('-'*20)
# print(soup.div)
# # 获取第一个div节点中的第一个img节点
# print('-'*20)
# print(soup.div.img)
# # 获取第一个div节点中的第一个img节点的属性
# print('-'*20)
# print(soup.div.img.attrs)
# # 获取第一个div节点中的第一个img节点的标签名
# print('-'*20)
# print(soup.div.img.name)
# # 获取第一个div节点中的第一个a节点的文本内容
# print('-'*20)
# print(soup.div.a.string)
# # 获取节点的中所有子节点
# #(1).contents 以列表的方式输出子节点
# print('-'*20)
# print(soup.div.contents)
# #(2).children 返回一个可迭代对象
# print('-'*20)
# for child in soup.div.children:
#     print(child)
# print('-'*20)
# #(3).descendants 获取子孙节点
# for child in soup.div.descendants:
#     print(child)

# for string_1 in soup.div.div.p.strings:
#     print(repr(string_1))
#
# for string_2 in soup.div.div.p.stripped_strings:
#     print(repr(string_2))

# # 获取父节点
# for parent in soup.div.div.p.parents:
#     print(parent.name)

# 获取兄弟点（同一级的其他相同标签的节点）
# privious_siblings 前面所有的兄弟节点
# for parent in soup.div.div.p.previous_siblings:
#     print('-' * 20)
#     print(parent.name)
# # next_siblings 后面所有的兄弟节点
# for parent in soup.div.div.p.next_siblings:
#     print('*' * 20)
#     print(parent.name)

#获取同一级的所有的前后节点
# for ele in soup.div.div.next_elements:
#     print(ele.name)
print(soup.div.div.img)