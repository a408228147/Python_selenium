from xml.dom import minidom

#打开xml文档
dom = minidom.parse('text.xml')

#得到文档元素对象
root=dom.documentElement

tagname = root.getElementsByTagName('browser')
print(tagname[0].firstChild.data)

tagname = root.getElementsByTagName('login')
print(tagname[1].getAttribute("username"))

tagname = root.getElementsByTagName('province')
print(tagname[1].firstChild.data)
print("-----------")
province = dom.getElementsByTagName('province')
city = dom.getElementsByTagName('city')
print(province[2].firstChild.data)
print(city[1].firstChild.data)

tagname=root.getElementsByTagName('city')
print(tagname[0].firstChild.data)