#!/usr/bin/env python
#-*- coding:utf-8 _*-
__author__ = 'LJjia'
# *******************************************************************
#     Filename @  demo.py
#       Author @  Jia Liangjun
#  Create date @  2021/02/11 11:33
#        Email @  LJjiahf@163.com
#  Description @  
# ********************************************************************

import os

def hash_func(value):
    return (value+2+(value<<1))%8^5

if __name__ == '__main__':
    print(hash_func(10))
    print(hash_func(10000))
    print(hash_func(100))
    print(hash_func(1024))

