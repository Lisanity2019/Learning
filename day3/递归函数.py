# -*- coding: utf-8 -*-

# 递归函数：在函数内部，如果一个函数在内部调用自身本身，这个函数就是递归函数
#最大递归深度默认997/998
#---->

# n=0
# def pro():
#     global n
#     n+=1
#     print(n)
#     pro()
#
# pro()

#---->
#如果递归次数太多，就不适合用递归来解决问题
#递归缺点：占内存空间
#递归优点：会让代码简单化
#---->

# 计算阶乘n! = 1 x 2 x 3 x ... x n
# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n*fact(n-1)
#
# print(fact(50))

#---->
# 可以通过 尾递归 方式来解决递归调用栈溢出问题 事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数
# 尾递归：是指，在函数返回的时候，调用自身本身，并且，return 语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，
# 使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

# 实际上python跟大多数其它语言一样，没有对尾递归进行优化。不过可以通过把原函数变成一个生成器
# 用一个方法让它不断执行生成器的__next__(), 达到优化，真正避免深度递归的时候栈溢出问题。
#---->
# 原始尾递归(仍然存在栈溢出问题)

# def fact(n):
#     return fact_iter(n,1)
#
# def fact_iter(num,product):
#     if num==1:
#         return product
#     return fact_iter(num-1,num*product)
#
# print(fact(999))

#---->
#修改后：
import time
def wrapper(func):
    def inner(*args,**kwargs):
        start=time.time()
        ret=func(*args,**kwargs)
        end=time.time()
        print(end-start)
        return ret
    return inner

def fact_iter(num,product=1):
    if num==1:
        yield product
    yield fact_iter(num-1,num*product)

import types

@wrapper
def tramp(gen, *args, **kwargs):
    g = gen(*args, **kwargs)
    while isinstance(g, types.GeneratorType):
        g=g.__next__()
    return g
print(tramp(fact_iter, 100000))

#---->
# 可以通过 尾递归 方式来解决递归调用栈溢出问题 事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数
# 尾递归：是指，在函数返回的时候，调用自身本身，并且，return 语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，
# 使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

# 实际上python跟大多数其它语言一样，没有对尾递归进行优化。不过可以通过把原函数变成一个生成器
# 用一个方法让它不断执行生成器的__next__(), 达到优化，真正避免深度递归的时候栈溢出问题。
#---->

#通过自定义的尾递归优化后，执行10万的阶乘，得到结果一个长整型大数，共有45.6万位数，执行时间仅3秒，而且每次递归不用再开辟内存空间
#而Python语言默认递归深度只有1000次左右，即使修改底层默认深度限制设置，但是仍然存在一个极限，且会一直开辟内存空间