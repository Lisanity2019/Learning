# -*- coding: utf-8 -*-

# concurrent.futures模块提供了高度封装的异步调用接口(没有同步）

# # 基本方法
# #submit(fn, *args, **kwargs)
# 异步提交任务
#
# #map(func, *iterables, timeout=None, chunksize=1) 拿不到返回值
# 取代for循环submit的操作
#
# #shutdown(wait=True)
# 相当于进程池的pool.close()+pool.join()操作
# wait=True，等待池内所有任务执行完毕回收完资源后才继续
# wait=False，立即返回，并不会等待池内的任务执行完毕
# 但不管wait参数为何值，整个程序都会等到所有任务执行完毕
# submit和map必须在shutdown之前
#
# #result(timeout=None)
# 取得结果
#
# #add_done_callback(fn)
# 回调函数
#
# # done()
# 判断某一个线程是否完成
#
# # cancle()
# 取消某个任务

import time
from concurrent.futures import ThreadPoolExecutor  # 线程池
from concurrent.futures import ProcessPoolExecutor  # 进程池


# ------------------------------------------->
# def func(n):
#     time.sleep(1)
#     print(n)
#     return n*n
#
# t_list=[]
# tpool=ThreadPoolExecutor()
# for i in range(20):
#     t=tpool.submit(func,i)
#     t_list.append(t)
#
# tpool.shutdown()  #相当于进程池的pool.close()+pool.join()操作
# print('主线程')
# for t in t_list:print('计算返回的结果为:%s'%t.result())
# ------------------------------------------->

def func(n):
    time.sleep(1)
    print(n)
    return n * n


def call_back(m):
    print('计算返回的结果是%s' % m.result())


tpool = ThreadPoolExecutor()
for i in range(20):
    tpool.submit(func, i).add_done_callback(call_back)

# tpool.shutdown()  #相当于进程池的pool.close()+pool.join()操作

print('主线程')
