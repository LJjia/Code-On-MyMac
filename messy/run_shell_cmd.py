#!/usr/bin/env python
# -*- coding:utf-8 _*-
__author__ = 'LJjia'
# *******************************************************************
#     Filename @  run_shell_cmd.py
#       Author @  Jia Liangjun
#  Create date @  2020/02/28 20:10
#        Email @  LJjiahf@163.com
#  Description @  通过subprocess模块执行shell命令
# ********************************************************************

import subprocess

# shell参数为false时传入的args为数组形式，第一个为命令，第二个为对应输入参数
ls1 = subprocess.Popen(['ls', '-l'], shell=False)
ls2 = subprocess.Popen('ls -l', shell=True)
