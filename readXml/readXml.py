#!/usr/bin/env python
# -*- coding:utf-8 _*-
__author__ = 'LJjia'
# *******************************************************************
#     Filename @  readXml.py
#       Author @  Jia Liangjun
#  Create date @  2020/09/15 23:04
#        Email @  LJjiahf@163.com
#  Description @  读写xml文件
# ********************************************************************


import xml.dom.minidom


def readXML():
    domTree = xml.dom.minidom.parse("./abc.xml")
    # 文档根元素
    rootNode = domTree.documentElement
    print(rootNode.nodeName)

    # 所有顾客
    customers = rootNode.getElementsByTagName("customer")
    print("****所有顾客信息****")
    for customer in customers:
        if customer.hasAttribute("ID"):
            print("ID:", customer.getAttribute("ID"))
            # name 元素
            name = customer.getElementsByTagName("name")[0]

            print(name.nodeName, ":", name.childNodes[0].data)
            # phone 元素
            phone = customer.getElementsByTagName("phone")[0]
            print(phone.nodeName, ":", phone.childNodes[0].data)
            # comments 元素
            comments = customer.getElementsByTagName("comments")[0]
            print(comments.nodeName, ":", comments.childNodes[0].data)


def writeXML():
    domTree = xml.dom.minidom.parse("./abc.xml")
    # 文档根元素
    rootNode = domTree.documentElement

    # 新建一个customer节点
    customer_node = domTree.createElement("customer")
    customer_node.setAttribute("ID", "C003")

    # 创建name节点,并设置textValue
    name_node = domTree.createElement("name")
    name_text_value = domTree.createTextNode("kavin")
    name_node.appendChild(name_text_value)  # 把文本节点挂到name_node节点
    customer_node.appendChild(name_node)

    # 创建phone节点,并设置textValue
    phone_node = domTree.createElement("phone")
    phone_text_value = domTree.createTextNode("32467")
    phone_node.appendChild(phone_text_value)  # 把文本节点挂到name_node节点
    customer_node.appendChild(phone_node)

    # 创建comments节点,这里是CDATA
    comments_node = domTree.createElement("comments")
    cdata_text_value = domTree.createCDATASection("A small but healthy company.")
    comments_node.appendChild(cdata_text_value)
    customer_node.appendChild(comments_node)

    rootNode.appendChild(customer_node)

    with open('added_customer.xml', 'w') as f:
        # 缩进 - 换行 - 编码
        domTree.writexml(f, indent='    ', newl='\t', addindent='  ', encoding='utf-8')


'''
writer是文件对象
indent是每个tag前填充的字符，如：’ ‘，则表示每个tag前有两个空格
addindent是每个子结点的缩近字符
newl是每个tag后填充的字符，如：’\n’，则表示每个tag后面有一个回车
encoding是生成的XML信息头中的encoding属性值，在输出时minidom并不真正进行编码的处理，
如果你保存的文本内容中有汉字，则需要自已进行编码转换。
writexml方法是除了writer参数必须要有外，其余可以省略。

作者：VeyronC
链接：https://www.jianshu.com/p/17386972a23b
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''


def chgXML():
    domTree = xml.dom.minidom.parse("./abc.xml")
    # 文档根元素
    rootNode = domTree.documentElement

    names = rootNode.getElementsByTagName("name")
    for name in names:
        if name.childNodes[0].data == "Acme Inc.":
            # 获取到name节点的父节点
            pn = name.parentNode
            # 父节点的phone节点，其实也就是name的兄弟节点
            # 可能有sibNode方法，我没试过，大家可以google一下
            phone = pn.getElementsByTagName("phone")[0]
            # 更新phone的取值
            phone.childNodes[0].data = 99999

    with open('updated_customer.xml', 'w') as f:
        # 缩进 - 换行 - 编码
        domTree.writexml(f, indent='\t', newl='\n', addindent='\t', encoding='utf-8')


if __name__ == '__main__':
    readXML()
    writeXML()
    chgXML()

'''
这篇博客
https://blog.csdn.net/qq_37174526/article/details/89489212
'''
