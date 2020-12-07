#!/usr/bin/env python
#-*- coding:utf-8 _*-
__author__ = 'LJjia'
# *******************************************************************
#     Filename @  yuv_displayer.py
#       Author @  Jia Liangjun
#  Create date @  2020/09/10 19:58
#        Email @  LJjiahf@163.com
#  Description @  yuv图片显示工具,显示代码
# ********************************************************************


import cv2
import numpy as np
import os


def disp_one_yuv_frame(filename, width, height,end=None):
    '''
    显示一帧的yuv图像
    :param filename:yuv文件名
    :param width:yuv图像宽
    :param height:yuv图像高
    :return:
    '''
    fp = open(filename, 'rb')

    framesize = height * width * 3 // 2  # 一帧图像所含的像素个数

    # 第二个参数：可选，默认值为0。给offset参数一个定义，表示要从哪个位置开始偏移；
    # 0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。
    fp.seek(0, 2)  # 设置文件指针到文件流的尾部
    file_size = fp.tell()  # 当前文件指针位置
    fp.seek(0, 0)

    # order表示行优先
    Yt = np.zeros(shape=(height*3//2, width), dtype='uint8', order='C')

    for m in range(height*3//2):
        for n in range(width):
            # 原本是字节串,需要将其转换为整数
            Yt[m, n] = ord(fp.read(1))

    img=Yt.astype('uint8')
    print(img.shape)
    # 由于 opencv 不能直接读取 YUV 格式的文件, 所以要转换一下格式,大致含义是说将yuv转换为bgr(nv12格式转换)
    bgr_img = cv2.cvtColor(img, cv2.COLOR_YUV2BGR_NV12)  # 注意 YUV 的存储格式
    # 0 表示不根据图像打消调整窗口大小
    cv2.namedWindow("YuvDisp", 0)
    cv2.imshow('YuvDisp',bgr_img)
    if(type(end)==type('q')):
        # chr()是将数字转化为ascii码,ord则是将ascii码转换为数字
        while(cv2.waitKey(200)!=ord(end)):
            pass
    elif (type(end)==type(100)):
        cv2.waitKey(end)
    else:
        # 默认等待1000ms
        cv2.waitKey(1000)
    cv2.destroyWindow("YuvDisp")

    fp.close()
    return None


def getYuvParam(cfg_file):
    fp=open(cfg_file)
    for line in fp.readline():
        pass

file_list=[x for x in os.listdir('.') if('data' in x )]
print("find file name list ",file_list)





if __name__ == '__main__':
    #_ = yuv2bgr(filename='xxx.yuv', height=1080, width=1920, startfrm=0)
    disp_one_yuv_frame('pic.yuv', 1920,1080,'q')




# 对于python中需要使用c语言结构体的,可以参考下面这个函数