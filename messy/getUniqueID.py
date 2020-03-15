#!/usr/bin/env python
#-*- coding:utf-8 _*-
__author__ = 'LJjia'
# *******************************************************************
#     Filename @  getUniqueID.py
#       Author @  Jia Liangjun
#  Create date @  2020/02/26 21:31
#        Email @  LJjiahf@163.com
#  Description @  主要研究python的UUID模块 UUID: 通用唯一标识符 Universally Unique Identifier
#                   也叫GUID Global Unique Identifier
# ********************************************************************
'''
UUID主要有五个算法，也就是五种方法来实现。
（1）. uuid1(node, clock_seq)---基于时间戳
　　由MAC地址，当前时间戳，随机数字生成。可以保证全球范围内的唯一性。但是由于MAC地址的使用同时带来了安全问题，
局域网中可以使用IP来代替MAC。函数有两个参数, 如果 node 参数未指定, 系统将会自动调用 getnode() 函数来获取主机的硬件地址.
如果 clock_seq 参数未指定系统会使用一个随机产生的14位序列号来代替
（2）. uuid2()---基于分布式计算环境DCE（python中没有这个函数）
　　算法和uuid1相同，不同的是把时间戳的前4位换位POSIX的UID，实际中很少用到该方法。
（3）. uuid3()---基于名字和MD5散列值
　　通过计算名字和命名空间的MD5散列值得到，保证了同一命名空间中不同名字的唯一性，和不同命名空间的唯一性，
但同一命名空间的名字生成相同的uuid。
（4）. uuid4()---基于随机数
　　由伪随机数得到，有一定的重复概率，该概率可以计算出来。
（5）. uuid5()---基于名字的SHA-1散列值
　　算法和uuid3()相同，不同的是使用Secure Hash Algorithm 1 算法。
uuid格式8-4-4-4-8 共32位二进制
'''
import uuid

def getUUID(func,*,node=None,clock_seq=None,name=None):
    '''
    :param func:函数类型，传入数字int类型 可选1,3,4,5
    :param node: 节点名称，uuid1使用，不传默认使用mac地址或网络地址
    :param clock_seq: 当前时间序列 uuid1使用，不传默认使用随机数(14位大小)
    :param namespace: 命名空间，当前使用个默认的，其实这个用哪个变量都没什么区别，随便写一个
    :param name: 输入的字符串名
    :return:
    '''
    if 1==func:
        unique_id=uuid.uuid1(node,clock_seq)
    elif 3==func:
        if name:
            namespace=uuid.NAMESPACE_DNS
            unique_id = uuid.uuid3(namespace,name)
        else:
            return None
    elif 4==func:
        unique_id=uuid.uuid4()
    elif 5==func:
        if name:
            namespace = uuid.NAMESPACE_DNS
            unique_id=uuid.uuid5(namespace,name)
        else:
            return None
    else:
        return None
    return str(unique_id)

if __name__ == '__main__':
    id=getUUID(3,name='DSP_VCA_WBR_PCI_TEST')
    print(id)

'd4552e0d-eaaf-38b9-b0c1-d301286af321'
'403447d7-01a4-3778-baf8-b30fc037cbb8'
'322dc45c-b96f-3822-b44b-7310ba568e46'