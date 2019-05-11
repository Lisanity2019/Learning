# -*- coding: utf-8 -*-

import time
import os
from multiprocessing import Process


def func(args, args2):
    print('子进程PID：', os.getpid())
    print('子进程的父进程PID：', os.getppid())
    print(args)
    time.sleep(3)
    print(args2)


p = Process(target=func, args=(1, 2))  # 创建进程对象,并传参
p.start()  # 开启子进程
print('主进程PID：', os.getpid())
print('*' * 10)

# ----> 进程的生命周期
# 主进程自己的代码如果长，等待自己的代码执行结束
# 子进程的执行时间长，主进程 会自己代码段执行完毕之后，等待子进程执行完毕之后，才会结束
