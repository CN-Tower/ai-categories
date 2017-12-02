from lxml import etree
file='demo1.xml'
#sel=etree.parse(file)#将xml解析为树结构
root=etree.fromstring(open(file=file).read().encode('utf-8')) # 接收 byte string
print(etree.tostring(root))# 默认返回的是 byte string
print(etree.tostring(root, pretty_print=True).decode('utf-8'))#decode 一下变成 utf-8
