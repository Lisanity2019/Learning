# -*- coding: utf-8 -*-

# ---->守护线程：子线程随着主进程代码执行完毕而结束  daemon=True


import time
from multiprocessing import Process


def func():
    while True:
        time.sleep(0.2)
        print('我还活着')


p = Process(target=func)
p.daemon = True  # 设置子进程为守护进程
p.start()
i = 0
while i < 5:
    print('我是服务端')
    time.sleep(1)
    i += 1
## p.is_alive()  检查子进程是否还存活
## p.terminate() 在主线程内结束一个子进程 结束一个子进程不是在执行方法之后立即生效，需要操作系统响应过程
## p.pid    子进程的PID
## p.name   子进程的名字
