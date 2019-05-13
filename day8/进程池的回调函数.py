# -*- coding: utf-8 -*-

# 回调函数

import os
import time
from multiprocessing import Pool


def func1(n):
    print('in func1 PID:%s' % os.getpid())
    return n * n


def func2(nn):
    time.sleep(1)
    print('in func2 PID:%s' % os.getpid())
    print(nn)


p = Pool()
print('主进程 PID:%s' % os.getpid())
for i in range(10):
    p.apply_async(func1, args=(10,), callback=func2)  # 回调函数不能传参
# 且回调函数是在主进程执行的
p.close()
p.join()
