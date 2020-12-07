#!/usr/bin/env python
#-*- coding:utf-8 _*-
__author__ = 'LJjia'
# *******************************************************************
#     Filename @  c_struct.py
#       Author @  Jia Liangjun
#  Create date @  2020/10/13 23:33
#        Email @  LJjiahf@163.com
#  Description @  读取C语言解结构体
# ********************************************************************

import struct

file=open("tmp.bin",'rb')
content=file.read(16)
real=struct.unpack('4I',content)
print(content)


'''
# struct打包方式
aaa=struct.pack('4I',1,2,3,4)
print(aaa)
'''

#这篇博客写的也很详细