#!/usr/bin/env python
# -*- coding:utf-8 _*-
__author__ = 'LJjia'
# *******************************************************************
#     Filename @  test2.py
#       Author @  Jia LiangJun
#  Create date @  2019/02/14 14:05
#        Email @  LJjiahf@163.com
#  Description @  
# ********************************************************************

from multiprocessing import Process
import os


# 子进程要执行的代码
def run_process(name):
    print('Run child process name:%s num(%s)' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process is %s' % (os.getpid()))
    p = Process(target=run_process, args=('test',))
    print('child process will start')
    #使用start方法启动子进程p
    p.start()
    #使用join方法等待子进程运行结束
    p.join()
    print('child process end')
