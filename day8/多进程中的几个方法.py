# -*- coding: utf-8 -*-

import time
from multiprocessing import Process


def func(arg1, arg2):
    print('*' * arg1)
    time.sleep(5)
    print('*' * arg2)


p = Process(target=func, args=(10, 20))
p.start()
p.join()  # join 等待子线程结束后，主进程才继续执行  异步变为同步
print('主进程运行完了！')
