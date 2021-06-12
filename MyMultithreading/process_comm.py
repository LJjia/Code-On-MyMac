#!/usr/bin/env python
#-*- coding:utf-8 _*-
__author__ = 'LJjia'
# *******************************************************************
#     Filename @  process_comm.py
#       Author @  Jia LiangJun
#  Create date @  2019/07/24 22:31
#        Email @  LJjiahf@163.com
#  Description @  使用queue和pipes方式来实现进程之间的通信
# ********************************************************************
from multiprocessing import Process,Queue
import os,time,random

# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__ == '__main__':
    # 父进程创建Queue 这相当于一个所有进程中共享的队列 并传递给每个子进程
    # 但是要注意 ，如果pw放完了，再执行pr好像pr就无法启动
    q=Queue()
    # 使用Process创建子进程
    pw=Process(target=write,args=(q,))
    pr=Process(target=read,args=(q,))
    # 一个进程往队列中写入，并且延时一段时间
    # 而另一个进程则立刻从队列中读取，数据读一次就消失
    pw.start()

    time.sleep(1)
    pr.start()
    # 等待pw结束
    pw.join()
    # 因为pr是死循环，因此只能强行停止pr
    pr.terminate()