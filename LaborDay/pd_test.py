#!/usr/bin/env python
#-*- coding:utf-8 _*-
__author__ = 'LJjia'
# *******************************************************************
#     Filename @  pd_test.py
#       Author @  Jia Liangjun
#  Create date @  2021/05/04 12:06
#        Email @  LJjiahf@163.com
#  Description @  pandas 实践教程
# ********************************************************************

import pandas as pd

df=pd.read_excel("team.xlsx")
# 显示每列是否有空数据
print(df.isnull().any())
# 显示表格信息
print(df.info())
# 查看数值型列的汇总统计
print(df.describe())
# 显示数据行和列名
# 显示列名
print(df.axes,'\n\n',df.columns)

df.set_index('name', inplace=True) # 建立索引并生效
print('\n\n\n',df.index)
print(df.head(3))

print(df[1:2])

