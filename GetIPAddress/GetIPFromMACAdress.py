#!/usr/bin/env python
#-*- coding:utf-8 _*-
__author__ = 'LJjia'
# *******************************************************************
#     Filename @  GetIPFromMACAdress.py
#       Author @  Jia Liangjun
#  Create date @  2020/02/25 23:26
#        Email @  LJjiahf@163.com
#  Description @  根据MAC地址获取IP地址，最终实践说明这个构想有点哈
#                 因为智能在局域网内根据查arp表 获取IP地址对应的mac地址
# ********************************************************************

import platform
import os
import subprocess
import time

# 平台的表示和我们实际认知的有所区别
# window-win32 linux-linux Windows/Cygwin-cygwin MacOS-Darwin(达尔文)
print(platform.system())
# 下面这个是打印各种信息的总的集合
# print(platform.uname())


def outputCmd(cmd):
    r = os.popen(cmd)
    text = r.read()
    r.close()
    return text


def checkDevice_and_writeInTxt():
    val = 0
    netport = 0
    print("稍等片刻，局域网设备搜索中......")
    print("************************************")
    f = open("IP_MAC.txt", "w+")
    for val in range(8, 9):
        dest_ip = "192.168.1." + val.__str__()
        print(dest_ip)
        cmd_pingAll = "ping "  + " -c 2 "+dest_ip
        result = outputCmd(cmd_pingAll)
        print(result)


child = subprocess.Popen(['ping','www.baidu.com'])
time.sleep(1)
print(child.stdout)
#child.wait()

if __name__ == '__main__':
    pass


