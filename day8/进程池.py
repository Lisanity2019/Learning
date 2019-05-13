# -*- coding: utf-8 -*-

# 效率问题
# ---->每次开启进程,都要开启这个进程的内存空间，耗时
# ---->进程过多，操作系统的调度

# 进程池 效率问题
# ---->python中 先创建一个进程池
# ---->进程池指定存放多少个进程
# ------------------------------------------->
# import time
# from multiprocessing import Process,Pool
#
# def func(n):
#     n+=1
#
# start=time.time()
# pool=Pool(8)
# pool.map(func,range(100))  #---->map自带join同步,传参必须是可迭代的
# end=time.time()
# runtime1=end-start
# print('使用进程池执行时间:%.4f'%runtime1)
#
# t1=time.time()
# p_list=[]
# for i in range(1000):
#     p=Process(target=func,args=(i,))
#     p_list.append(p)
#     p.start()
#
# for p in p_list:p.join()
# t2=time.time()
# runtime2=t2-t1
#
# print('使用创建进程执行时间:%.4f'%runtime2)
# print('执行时间：进程池方式比创建进程方式快 %.2f 倍'%(runtime2/runtime1))

# ---->执行时间：当子进程数量很多的时候，进程池方式比创建进程方式快
# ------------------------------------------->

import os
import time
from multiprocessing import Pool


# print(os.cpu_count()) #系统CPU个数

def func(n):
    print('start func %s' % n, '子进程PID:%s' % os.getpid())
    time.sleep(1)
    print('end func %s' % n, '子进程PID:%s' % os.getpid())


p = Pool(3)
for i in range(10):
    # p.apply(func,args=(i,))  #apply 使用同步方法提交任务，当创建的子进程
    # 结束后，主进程才会继续执行
    p.apply_async(func, args=(i,))  # apply_async 异步提交任务，需要手动
# close和join
p.close()  # 结束进程池接受任务
p.join()  # 感知进程池中的任务全部执行完毕，全部执行完毕后，主进程才会继续执行

# ----> 进程池创建的子进程是先在进程池创建好指定数量的子进程,然后把执行的函数
# 放入进程池创建好的子进程里,从始至终只有开始指定的进程数.
