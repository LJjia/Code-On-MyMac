#!/usr/bin/env python
#-*- coding:utf-8 _*-
__author__ = 'LJjia'
# *******************************************************************
#     Filename @  use_pandas.py
#       Author @  Jia Liangjun
#  Create date @  2021/05/04 11:54
#        Email @  LJjiahf@163.com
#  Description @  使用pandas处理csv数据
# ********************************************************************

import pandas as pd
import pprint
df=pd.read_csv("examples.txt")
print("disp result")
print(df.isnull().any())
print(df.info())



