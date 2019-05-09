# -*- coding: utf-8 -*-

# ----> 反射
# hasattr getattr delattr setattr

# hasattr(类名或对象，变量或方法名字符串) 判断命名空间是否存在相应变量
# getattr(类名或对象，变量或方法名字符串) 获取这个变量

class A:
    dic = {'name': 'user', 'password': 'pwd'}

    def a(self):
        print('a')


# person=A()

if hasattr(A, 'dic'):
    ret = getattr(A, 'dic')
    print(ret)
else:
    print('没有该变量或方法')

# ----> 反射：用字符串类型的名字 去操作 变量
# ----> 反射同样适用于模块中的变量或方法
