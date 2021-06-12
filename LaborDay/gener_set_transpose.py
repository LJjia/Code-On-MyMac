#!/usr/bin/env python
#-*- coding:utf-8 _*-
__author__ = 'LJjia'
# *******************************************************************
#     Filename @  draw_venn.py
#       Author @  Jia Liangjun
#  Create date @  2021/05/04 16:22
#        Email @  LJjiahf@163.com
#  Description @  画vnn图
# ********************************************************************

from matplotlib_venn import venn2
from matplotlib import pyplot as plt
import pandas as pd
import pprint


jizhi_df=pd.read_csv('jizhi.csv')
jizhi_select_name=jizhi_df[jizhi_df['change']=='DOWN']['name']


immunity_df=pd.read_csv('immunity.csv')
immunity_select_name=immunity_df[immunity_df['change']=='DOWN']['name']


jizhi_set=set(jizhi_select_name)
immunity_set=set(immunity_select_name)

total = len(jizhi_set.union(immunity_set))
print('total data num %s jizhi %s immunity %s'%(total,len(jizhi_set),len(immunity_set)))
same_ele_set=(jizhi_set&immunity_set)
# 打印相同元素列表
# pprint.pprint(same_ele_set)

# 画venn图
# venn2(subsets=[jizhi_set,immunity_set],set_labels=('jizhi','mianyi'),set_colors=('r','g'),subset_label_formatter=lambda x: f"{(x/total):1.0%}")
# plt.show()

# immunity_df[immunity_df['logFC']=='ZNF804A']
print('set len ',len(list(same_ele_set)))
big_src_data_matrix=pd.read_csv('result.txt',sep='\t',low_memory=False)
print(big_src_data_matrix.info())
out_matrix=big_src_data_matrix.loc[list(same_ele_set)]
print(out_matrix)
out_matrix.transpose().to_csv('out_transpose_csv.txt',sep='\t')

