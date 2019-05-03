# -*- coding: utf-8 -*-
__author__ = 'liyao'


def wrapper1(func): #func-->inner2
    def inner1(*args, **kwargs):
        print('wrapper1,before func')
        ret = func()
        print('wrapper1,after func')
        return ret

    return inner1


def wrapper2(func): #func-->f
    def inner2(*args, **kwargs):
        print('wrapper2,before func')
        ret = func()
        print('wrapper2,after func')
        return ret

    return inner2


@wrapper1  # f=wrapper1(f)-f被下一行赋值修改为inner2->f=wrapper1(inner2)==inner1 执行inner1,func调用的是inner2
@wrapper2  # f=wrapper2(f)=inner2
def f():
    print('function')


f() #-->inner1
