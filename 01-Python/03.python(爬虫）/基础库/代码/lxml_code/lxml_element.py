from lxml import etree
import codecs
file='demo1.xml'
#sel=etree.parse(file)#将xml解析为树结构
root=etree.fromstring(open(file=file).read().encode('utf-8')) # 接收 byte string
print(root.tag) # 首节点节点
print(root[0].tag)#第一个内节点
article = root[0]
#显示属性
print(article.attrib)
print(article.get('key'))

#获得一个节点对应的树
t = root.getroottree()
print(t.getroot()==root)#使用getroot 返回一个树的根节点
foo_tree = etree.ElementTree(root)#可以从一个节点构造一个树，那么这个节点就是这棵树的根
print(foo_tree.getroot().tag)#获取根

#添加子节点
child1 = etree.SubElement(root, 'child1')
child2 = etree.SubElement(root, 'child2')
child3 = etree.SubElement(root, 'child3')

#删除子节点
root.remove(child1)  # 删除指定子节点
print(etree.tostring(root))
#root.clear()  # 清除所有子节点
#print(etree.tostring(root))

#以列表的方式操作子节点
child = root[0]  # 下标访问
print(child.tag)
print(len(root))  # 子节点数量
root.index(child2)  # 获取索引号
for child in root:  # 遍历
    print(child.tag)

root.insert(0, etree.Element('child0'))  # 插入
start = root[:1]  # 切片
end = root[-1:]

print(start[0].tag)
print(end[0].tag)

root.append( etree.Element('child4') )  # 尾部添加
print(etree.tostring(root))

#获取父节点
print(child1.getparent().tag)

#属性操作
#1.创建属性
root = etree.Element('root', interesting='totally')
print(etree.tostring(root))
root.set('hello', 'Huhu')
print(etree.tostring(root))

#2. 获取属性
print(root.get('interesting'))# get方法获得某一个属性值
print(sorted(root.keys()))# keys方法获取所有的属性名

# items方法获取所有的键值对
for name, value in sorted(root.items()):
    print('%s = %r' % (name, value))


#文本操作
#1. text和tail属性
root = etree.Element('root')
root.text = 'Hello, World!'
print(root.text)
print(etree.tostring(root))