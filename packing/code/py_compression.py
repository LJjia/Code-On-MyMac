#!/usr/bin/env python
#-*- coding:utf-8 _*-
__author__ = 'LJjia'
# *******************************************************************
#     Filename @  py_compression.py
#       Author @  Jia Liangjun
#  Create date @  2020/03/09 22:23
#        Email @  LJjiahf@163.com
#  Description @  尝试python的各种压缩文件
# ********************************************************************


import zipfile
import os

#压缩类型 有zip, gzip 7z等
compress_type='zip'

#突然想写面向对象算法了
class DataFile(object):
    def __init__(self,path,compress_type):
        if not os.path.exists(path):
            print('文件不存在')
            raise FileNotFoundError
        self.path=path
        self.compress_type=compress_type


    def compress(self,outputfile=None):
        if self.compress_type=='zip':
            if not outputfile:
                outputfile=self.path+'.zip'
            # 不给出ZIP_DEFLATED则只是进行存储,不压缩
            zip=zipfile.ZipFile(outputfile,'w',zipfile.ZIP_DEFLATED)
            '''
            os.walk经常用for循环来调用,得到一个三元组
            第一个为起始路径，第二个为起始路径下的文件夹，第三个是起始路径下的文件。
            dirpath 是一个string，代表目录的路径，
            dirnames 是一个list，包含了dirpath下所有子目录的名字。
            filenames 是一个list，包含了非目录文件的名字。
            '''
            for path, dirnames, filenames in os.walk(self.path):
                # 下面这行可以更改在源文件zip中文件的存放路径(其实多余)
                file_path_in_zip=path.replace(self.path,'')
                for filename in filenames:
                    #两个参数 源文件位置,放到压缩包里的文件位置
                    zip.write(os.path.join(path, filename), os.path.join(file_path_in_zip , filename))
            print('压缩成功')
            zip.close()

class CompressFile(DataFile):

    # def __init__(self,path,compress_type):
    #     if not os.path.exists(path):
    #         print('文件不存在')
    #         raise FileNotFoundError
    #     self.path=path
    #     self.compress_type = compress_type

    def uncompress(self,unzip_path='.'):
        if self.compress_type=='zip':
            if unzip_path!='.':
                if not os.path.isdir(unzip_path):
                    raise ValueError
                if os.path.exists(unzip_path):
                    raise FileExistsError
            datapack=zipfile.ZipFile(self.path,'r')

            foldername=unzip_path+'/'+os.path.basename(self.path)
            if foldername[-4:]==".zip":
                foldername=foldername[:-4]
            for file in datapack.namelist():
                # 以下两种都可以 解压可以设置解压地址
                #datapack.extractall(path=foldername)
                datapack.extract(member=file,path=foldername)
            print("解压成功")



if __name__ == '__main__':
    # folder=DataFile('../data','zip')
    # folder.compress()
    datapack=CompressFile('../data3.zip','zip')
    datapack.uncompress()
