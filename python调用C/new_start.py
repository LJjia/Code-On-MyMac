#!/usr/bin/env python
#-*- coding:utf-8 _*-
__author__ = 'LJjia'
# *******************************************************************
#     Filename @  new_start.py
#       Author @  Jia Liangjun
#  Create date @  2020/02/13 14:38
#        Email @  LJjiahf@163.com
#  Description @  因为工作需求，因此学习一下Python调用C语言的方法
# ********************************************************************

from ctypes import cdll

sum_dll=cdll.LoadLibrary('./c_source/sum_ab.so')
print(sum_dll.sum)
result=sum_dll.sum(5,6)
