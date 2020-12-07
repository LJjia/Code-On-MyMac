#!/usr/bin/env python
#-*- coding:utf-8 _*-
__author__ = 'LJjia'
# *******************************************************************
#     Filename @  test.py
#       Author @  Jia Liangjun
#  Create date @  2020/10/28 21:37
#        Email @  LJjiahf@163.com
#  Description @  测试mac的struss工具,监测进程
# ********************************************************************

import time

while True:
    file=open('new.txt','w')
    file.write('hello world\n')
    time.sleep(1)
    file.close()
    time.sleep(1)


