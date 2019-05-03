# -*- coding: utf-8 -*-

# Lambda函数，是一个匿名函数，创建语法：
#  lambda parameters:express
# parameters：可选，如果提供，通常是逗号分隔的变量表达式形式，即位置参数。
# expression：不能包含分支或循环（但允许条件表达式），也不能包含return（或yield）函数。如果为元组，则应用圆括号将其包含起来

# add=lambda x,y:x+y
# print(add(1,2))

#---->筛选字典最大value对应的keys
# dic={'k1':10,'k2':100,'k3':30}
# print(max(dic,key=lambda keys:dic[keys]))
# l=[1,2,3,4]
# print(list(filter(lambda x:x>2,l))) #---->filter
# print(list(map(lambda x:x**2,l)))  #---->map

# 现有两个元组(('a'),('b')),(('c'),('d'))，使用python中匿名函数生成列表[{'a':'c'},{'b':'d'}]
# t1=(('a'),('b'))
# t2=(('c'),('d'))
# test=lambda t1,t2:[{i,j} for i,j in zip(t1,t2)]
# print(test(t1,t2))