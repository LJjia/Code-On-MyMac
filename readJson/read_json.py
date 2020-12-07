#!/usr/bin/env python
#-*- coding:utf-8 _*-
__author__ = 'LJjia'
# *******************************************************************
#     Filename @  read_json.py
#       Author @  Jia Liangjun
#  Create date @  2020/09/14 21:58
#        Email @  LJjiahf@163.com
#  Description @  读取并解析json文件
# ********************************************************************


import json

# 将字典序列化为json字符串
data = {
    'name' : 'ACME',
    'shares' : 100,
    'price' : 542.23
}
# dumps是将python的字典和list对象序列化为json字符串
json_str = json.dumps(data)
print(json_str)

# 将python的字典对象直接保存为json文件
# with open('data.json', 'w') as f:
#     # 参数sort_key是说json元素是否以字符顺序排序,indent表示字符前面是否空几个空格,0为默认,只输出一行
#     json.dump(data, f,sort_keys=True,indent=4)


# 读取的时候,最好以utf-8编码格式读,否则mac会默认以ascii读 windows好像是gbk读取,遇到中文等特殊字符会报错
with open("data.json",encoding='utf-8') as load_f:
    load_dict = json.load(load_f)
    print(load_dict)

# 用于将str类型的数据转成dict
# data_loads=json.loads(json_str)
# print(data_loads)