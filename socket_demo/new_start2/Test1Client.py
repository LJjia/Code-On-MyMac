#!/usr/bin/env python
#-*- coding:utf-8 _*-
__author__ = 'LJjia'
# *******************************************************************
#     Filename @  Test2Client.py
#       Author @  Jia LiangJun
#  Create date @  2019/07/29 23:58
#        Email @  LJjiahf@163.com
#  Description @  客户端的socket程序
# ********************************************************************
import socket
import time
def create_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 8001))
    # 推迟执行
    time.sleep(2)
    s.send(b'1')
    print(s.recv(1024).decode('utf-8'))
    s.close()

if __name__ == '__main__':
   create_client()