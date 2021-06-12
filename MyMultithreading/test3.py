#!/usr/bin/env python
#-*- coding:utf-8 _*-
__author__ = 'LJjia'
# *******************************************************************
#     Filename @  test3.py
#       Author @  Jia LiangJun
#  Create date @  2019/07/24 22:07
#        Email @  LJjiahf@163.com
#  Description @  使用Processing创建子进程 （windows上不支持fork调用）
# ********************************************************************
from multiprocessing import Process
import os
#子进程要执行的代码
def run_proc(name):
    print('run child process %s (%s)'%(name,os.getpid()))

if __name__ == '__main__':
    print('Parent process is %s'%os.getpid())
    # 创建Process实例，传入执行函数和函数的参数。此步骤相当于fork出一个子进程
    p=Process(target=run_proc,args=('test',))
    print('child process start ')
    # 使用strat方法启动
    p.start()
    # join()方法等待子进程结束后再继续往下运行，通常用于进程之间的同步
    p.join()
    print('child process end')