from multiprocessing import Pool
import os,time,random

def long_time_task(name):
	print('Run task %s (%s)'%(name,os.getpid()))
	start=time.time()
	time.sleep(random.random()*3)
	end=time.time()
	print('Task %s run %0.2f seconds'%(name,(end-start)))

if __name__=='__main__':
	print('Parent process %s.'%os.getpid())
	# Pool()函数可创建同时执行的线程
	# 默认可分出的线程为CPU线程数 该台笔记本4核8线程
	# 因此如果i循环到9 可看到0-7个线程先跑,线程8等到其中某个线程跑完了才可以继续跑
	p=Pool()
	for i in range(6):
		p.apply_async(long_time_task,args=(i,))
	#注意 这个主函数的线程和pool分出的线程不是一个线程,因此打印的顺序只看哪个线程跑的快
	#看谁先抢占串口
	print('Waiting for all subprocesses done...')
	p.close()
	p.join()
	print('All subprocesses done')