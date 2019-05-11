# -*- coding: utf-8 -*-

import time
import os
from multiprocessing import Process


# ------------------------------------------->
# 每创建一个子进程，等待该子线程结束后，继续创建子线程并执行，循环
# def func(arg1,arg2):
#     print('子进程PID：',os.getpid(),'*'*arg1)
#     time.sleep(1)
#     print('子进程PID：',os.getpid(),'*'*arg2)
#
# for i in range(8):
#     p=Process(target=func,args=(5*i,10*i))
#     p.start()
#     p.join()   #join 在这里，创建第一个子进程后，等待该子进程执行结束后主进程才会继续执行，这里是执行创建下一个子进程
#
# print('主进程运行完了！')
# ------------------------------------------->
# 同时创建多个进程并启动，异步运行，然后让所有异步的子线程都结束后，才继续执行主线程的代码段
def func(arg1, arg2):
    print('子进程PID：', os.getpid(), '*' * arg1)
    # time.sleep(1)
    print('子进程PID：', os.getpid(), '*' * arg2)


p_list = []
for i in range(8):
    p = Process(target=func, args=(5 * i, 10 * i))
    p.start()
    p_list.append(p)
[p.join() for p in p_list]
print('主进程运行完了！')
# ------------------------------------------->
