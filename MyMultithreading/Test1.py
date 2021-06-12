#!/usr/bin/env python
#-*- coding:utf-8 _*-
__author__ = 'LJjia'
# *******************************************************************
#     Filename @  Test1.py
#       Author @  Jia LiangJun
#  Create date @  2019/02/14 13:52
#        Email @  LJjiahf@163.com
#  Description @  多线程的测试样例
# ********************************************************************
import os

print('process (%s) start'%(os.getpid()))

pid=os.fork()
if pid==0:
    print('I am process %s and my parent is proceess %s'%(os.getpid(),os.getppid()))
else:
    print('I (%s) just created a child process (%s)'%(os.getpid(),pid))