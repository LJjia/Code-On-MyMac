#!/usr/bin/env python
#-*- coding:utf-8 _*-
__author__ = 'LJjia'
# *******************************************************************
#     Filename @  first_test.py
#       Author @  Jia Liangjun
#  Create date @  2020/05/21 23:35
#        Email @  LJjiahf@163.com
#  Description @  
# ********************************************************************

import imageio

video_file='mahatma.mp4'
#这有个使用imageio的简单样例
#https://www.jb51.net/article/138270.htm
#这是官网用例
#https://imageio.readthedocs.io/en/latest/examples.html

# 视频的绝对路径
filename = 'video/01_01.wmv'
# 可以选择解码工具
vid = imageio.get_reader(filename, 'ffmpeg')
for num, im in enumerate(vid):
    # image的类型是mageio.core.util.Image可用下面这一注释行转换为arrary
    print(im.mean())
    image = skimage.img_as_float(im).astype(np.float64)
    fig = pylab.figure()
    fig.suptitle('image #{}'.format(num), fontsize=20)
    pylab.imshow(im)
pylab.show()