# -*- coding: utf-8 -*-

# 第一种 直接通过实例化Process类
# 第二种 通过创建一个类继承Process类，实现run方法,run方法中是子进程要执行的代码段

import os
from multiprocessing import Process


class MyProcess(Process):
    def __init__(self, arg1, arg2):
        super().__init__()  # 传入父类初始化
        self.arg1 = arg1
        self.arg2 = arg2

    def run(self):
        print('子进程PID：', self.pid)
        print('子进程名称：', self.name)
        print(self.arg1)
        print(self.arg2)


print('主进程PID：', os.getpid())
p = MyProcess(1, 2)

p.start()
