import subprocess
import os 
# subprocess.call函数相当于在命令行中输入 nslookup python
# subprocess.call 相当于直接在命令行中输入命令,此函数输入参数为list,
# list中元素为 指令,输入参数
# nslookup用于查询DNS的记录，查询域名解析是否正常，在网络故障时用来诊断网络问题
r=subprocess.call(['nslookup','www.python.org'])
print('Exit Code:',r)
p=subprocess.call(['ls','-l'])

# 对于子进程还需要输入其他参数的情况
# 以下代码相当于在命令行中输入nslookup,然后手动输入
# set q=mx
# python.org
# exit

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)