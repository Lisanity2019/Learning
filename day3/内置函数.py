# -*- coding: utf-8 -*-
__author__ = 'liyao'

# 作用域 locals() globals()
#
# print(locals())  #---->返回本地作用域中所有变量字典
# print(globals()) #---->返回全局作用域中所有变量字典
# global 变量  #---->声明全局变量，如果在局部要对全局变量修改，需要在局部也要先声明该全局变量
# nonlocal 变量 #---->nonlocal关键字用来在函数或其他作用域中使用外层(非全局)变量
#
# next(迭代器) 内部实际调用的是迭代器.__next__()
# iter(可迭代对象）---->迭代器=可迭代对象.__iter__()
# range()  可迭代对象
#
# dir() ---->查看一个变量拥有的方法
# help() ---->查看数据类型帮助文档
#
# print(callable(print))   #callable() ---->检测函数名是否可调用
#
# import 导入---->实质是用内置 __import__()导入
# time=__import__('time')
# print(time.time())
#
# 如果某个方法不依赖任何数据类型，就直接调用 ---->内置函数 和自定义函数
# 某个方法属于某个数据类型的变量，就用.调用
#
# f=open('filename')   #打开文件，判断是否可读写
# print(f.writable())
# print(f.readable())
#
#
# 1.hash()返回对象的哈希值，用整数表示。哈希值在字典查找时，可用于快速比较键的值相等的数值
# 2.即使类型不一致，计算的哈希值是一样的
# print(hash(1))
# print(hash(1.0))
# print(hash([])) #列表不可哈希
#
# dict={1:'aaa',1.0:'bbbb'}
# print(dict)  #打印结果{1: 'bbbb'} 主键1和1.0的哈希值是一样的，后面的相同哈希值的key对应的值会覆盖之前的key对应的值
#
# input() 交互输入
# print('打印输出:\n',1,2,3,end='',sep='****')  #print(self, *args, sep=' ', end='\n', file=None)
# with open('file','w',encoding='utf-8') as f:  #打印到文件
#     print('打印输出:\n',1,2,3,end='',sep='****',file=f)
#
# 打印进度条
# import time
# for i in range(0,101,2):
#     time.sleep(0.1)
#     per_str='\r%s%% : %s\n' %(i,'*'*i) if i==100 else '\r%s%% : %s' %(i,'*'*i)
#     print(per_str,end='')
#
# exec eval compile编译
# eval() 函数和 exec() 函数的区别：
# eval() 函数只能计算单个表达式的值，而 exec() 函数可以动态运行代码段
# eval() 函数可以有返回值，而 exec() 函数返回值永远为 None
# exec('print(123)')
# eval('print(123)')
# print(exec('1+2+3'))
# print(eval('1+2+3'))

#数学运算
# print(bin(10))  #二进制
# print(oct(10))  #八进制
# print(hex(10))  #十六进制

# print(abs(-7)) #---->绝对值
# print(divmod(7,2)) #---->求除法商和余，返回元组
# print(round(3.1415,2)) ##---->四舍五入
# print(pow(2,3))  #---->2**3
# print(sum([1,2,3])) #---->求和，传入可迭代对象   sum([1,2,3],10) 从从10开始求和
# print(min(1,2,3,-4))

#数据类型：int bool .....
#数据结构：dict list tuple set str

# reversed()  #---->将原有列表元素进行反转
# list=[1,2,3,4,5]
# # list.reverse()
# list2=reversed(list) #---->不改变原有列表，但返回一个反序迭代器对象，节省了内存空间
# print(list2)

#bytes 转换成bytes类型
# 编码解码
# print( bytes('你好',encoding='gbk').decode('gbk'))
# print( bytes('你好',encoding='utf-8')) #---->unicode转utf-8

# print(ord('a'))  #---->字符按unicode转数字
# print(chr(97))  #---->数字按unicode转字符
# print(ascii('a')) #---->只要是ascii码中的内容就打印出来，不是就转换成\u

# print(repr('1')) #---->用于%r格式化输出
# print(repr(1))

# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# print(enumerate(seasons)) #---->返回枚举对象
# for i,element in enumerate(seasons,start=7): #---->for循环使用enumerate可以同时拿到索引,同时start参数可以指定索引起始值
#     print(i,element)

# all() #---->判断是否有bool值为False，有一个为False则为False
# any() #---->判断是否有bool值为True，有一个为True则为True

#---->zip() ；拉链函数，返回一个对象，支持多种数据结构，可将多个拉到一起，但是遵循对齐规则（聚合到长度最小的为止），字典只能拉取到key的值

# a=[1,2,3,4]
# b=['a','b','c']
# c=('a','b')
# d={"key1":"aa","key2":"bb"}
# print(zip(a,d,b))
# for i in zip(a,d,b):
#     print(i)

# filter() #---->函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素
# 语法： filter(function, iterable)  返回值：对象，显示需用list列表强转
# def is_odd(n):
#     return n % 2 == 1
#
# newlist =list(filter(is_odd,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# print(newlist)

# map()函数
# map()是 Python 内置的高阶函数，它接收一个函数 f 和一个 list，并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回
# 注意：map()函数不改变原有的 list，而是返回一个新的 list对象,同filter一样，需要list强转
# def f(x):
#     return x*x
# l=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(map(f,l))
# print(list(map(f, l)))
# print(l)

# sort() 在原有列表中排序，函数用于对原列表进行排序，reverse参数 -- 排序规则，reverse = True 降序， reverse = False 升序（默认）
# l=[1, 2, 3, 4, -5, 6, 7, 8, 9]
# l.sort(key =abs,reverse=True)
# print(l)

