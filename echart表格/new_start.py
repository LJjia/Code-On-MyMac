#!/usr/bin/env python
#-*- coding:utf-8 _*-
__author__ = 'LJjia'
# *******************************************************************
#     Filename @  new_start.py
#       Author @  Jia Liangjun
#  Create date @  2020/02/14 13:55
#        Email @  LJjiahf@163.com
#  Description @  使用python的pyechart表格 顺便尝试能不能加进我的reveal.js里
#                 因为版本更新不兼容的问题，0.5的
# ********************************************************************

'''
# 原始版本使用方法
from pyecharts import Map

value = [10, 80, 50]
attr = ['安徽', '浙江', '上海']
map = Map('Map 结合 VisualMap 实例', width=1920, height=1080)
map.add('china', attr, value, maptype='china',
        is_visualmap=True, visual_text_color='#F00',)
map.add('安徽', attr, value, maptype='安徽',
        is_visualmap=True, visual_text_color='#F0d',)

map.use_theme("vintage")
map.render()
'''

from pyecharts.charts import Bar,Graph
from pyecharts import options as opts
from pyecharts.globals import ThemeType

# V1 版本开始支持链式调用
# init_opts=opts.InitOpts设置主题和宽高，其可以进定义看一下有哪些参数可以设置，宽高是以字符串数字+px形式
bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK,width="1920px",height="1080px"))
    .add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
    .add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
    .set_global_opts(title_opts=opts.TitleOpts(title="某商场销售情况"))
)
bar.render('test.html')

#
# # 不习惯链式调用的开发者依旧可以单独调用方法
# bar = Bar()
# bar.add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
# bar.add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
# bar.add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
# bar.set_global_opts(title_opts=opts.TitleOpts(title="某商场销售情况"))
# bar.render()


