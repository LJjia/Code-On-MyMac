#!/usr/bin/env python
#-*- coding:utf-8 _*-
__author__ = 'LJjia'
# *******************************************************************
#     Filename @  liquid_charts.py
#       Author @  Jia Liangjun
#  Create date @  2020/02/16 21:57
#        Email @  LJjiahf@163.com
#  Description @  水球图绘制
# ********************************************************************

from pyecharts import options as opts
from pyecharts.charts import Grid, Liquid
from pyecharts.commons.utils import JsCode
from pyecharts.globals import SymbolType

l1 = (
    Liquid(init_opts=opts.InitOpts(width="1000px",height="1000px"),)
    .add("lq", [0.6, 0.7], center=["60%", "50%"])
    .set_global_opts(
        title_opts=opts.TitleOpts(title="多个 Liquid 显示"))
)

# 人口密度分布的最大最小参数配置.set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=400,min_=0)

# 第2个参数[0.5,0.55,0.6]有几个就表示有几条波纹，这个列表重的第一个值显示在最下面，最后一个值显示在最上面
# center对应的是图表显示在整个画布的什么位置，百分比形式表示
l2 =Liquid().add("lq",[0.5,0.45,0.4],center=["25%", "50%"],
    is_animation=True,
    label_opts=opts.LabelOpts(font_size=40,position="inside",),
    is_outline_show = False)



grid = Grid().add(l1, grid_opts=opts.GridOpts()).add(l2, grid_opts=opts.GridOpts())
grid.render()