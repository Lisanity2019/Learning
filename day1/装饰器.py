# -*- coding: utf-8 -*-
__author__ = 'liyao'


FLAG=False

def login(func):
    def inner(*args,**kwargs):
        '''
        登录程序装饰器
        '''
        with open('day1/log.txt','a',encoding='utf-8') as f:
            f.write(func.__name__+'\n') #将调用的函数写入文件
        global FLAG
        if FLAG:
            ret=func(*args,**kwargs)
            return ret
        else:
            username=input('请输入用户名:')
            password=input('请输入密码：')
            if username=='admin' and password=='admin':
                FLAG=True
                ret = func(*args, **kwargs)
                return ret
            else:
                print('登录失败！')
    return inner


@login
def shoplist_add():
    print('添加物品！')
@login
def shoplist_del():
    print('删除一件物品！')

shoplist_add()
shoplist_del()