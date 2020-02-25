#!/usr/bin/env python
#-*- coding:utf-8 _*-
__author__ = 'LJjia'
# *******************************************************************
#     Filename @  Test1Service.py
#       Author @  Jia LiangJun
#  Create date @  2019/07/29 23:57
#        Email @  LJjiahf@163.com
#  Description @  服务器端的socket程序
# ********************************************************************
import socket

def create_socket():
    # 创建socket对象s，基于internet地址和tcp协议
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定到本地的8001端口
    s.bind(("127.0.0.1", 8001))
    # 在本地8001端口监听，等待连接队列最大长度为5
    s.listen(5)
    print("等待连接")
    while True:
        # 接收来自客户端的连接
        connection,address=s.accept()
        try:
            # 设置5s内如果连接不上则超时
            connection.settimeout(5)
            # 接收客户端消息 消息长度为1024 编码为utf-8
            buf = connection.recv(1024).decode('utf-8')
            if buf == '1':
                connection.send(b'welcome to server')
            else:
                connection.send(b'please go out')
        except s.timeout:
            print('time out')
        finally:
            # 接收成功一次，则就关闭这次连接，等待下一个while循环再次接收
            connection.close()

if __name__ == '__main__':
    create_socket()