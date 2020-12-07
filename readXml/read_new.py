#!/usr/bin/env python
#-*- coding:utf-8 _*-
__author__ = 'LJjia'
# *******************************************************************
#     Filename @  read_new.py
#       Author @  Jia Liangjun
#  Create date @  2020/09/15 23:39
#        Email @  LJjiahf@163.com
#  Description @  读取新闻的xml,这个比较复杂
# ********************************************************************

from xml.dom.minidom import parse
import xml.dom.minidom
#dom解析xml
DOMTree = xml.dom.minidom.parse("new.xml")
#返回文档的根节点
root1 = DOMTree.documentElement
#观察新闻发现，内容都在Event元素下
ContentNodes = root1.getElementsByTagName("Event")
#定义一个字符串，保存解析出的数据
content = ""
#遍历所有的Event
for i in range(len(ContentNodes)):
    #获取第i个Event下的子节点
    SonNodes = ContentNodes[i].childNodes
    #遍历Event下的所有子节点
    for j in range(len(SonNodes)):
        # print(SonNodes[j].nodeName)
        if (SonNodes[j].nodeName != "#text"):
            content += SonNodes[j].firstChild.data
            # 获取所有Event下的值，不包含在Event子节点的值
        if (ContentNodes[i].childNodes[j].nodeValue != None):
            content += ContentNodes[i].childNodes[j].nodeValue

print(content)

'''
这篇博客
https://blog.csdn.net/snow_maple521/article/details/92794341?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.edu_weight&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.edu_weight
'''