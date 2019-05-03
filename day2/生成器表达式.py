# -*- coding: utf-8 -*-
__author__ = 'liyao'

#列表推导式
# eggs_list=['鸡蛋%s' %i for i in range(1,6)]
# print(eggs_list)


#生成器表达式
# g=(i for i in range(1,6))  #---->返回一个生成器对象,几乎不占用内存     列表表达式返回值，占用内存
# print(g)

# g=(i**2 for i in range(1,6) if i>=4)
# for i  in g:print(i)


# 列表推导式
#找到嵌套列表中名字含有两个‘e’的所有名字
# names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
#          ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
# print([name for lst in names for name in lst if name.count('e')>=2])

# 字典推导式

# 将一个字典的key和value对调
# mcase = {'a': 10, 'b': 34}
# print({mcase[key]:key for key in mcase})

# 合并大小写对应的 value 值，将 k 统一成小写
# mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
# print({key.lower():mcase.get(key.lower(),0)+mcase.get(key.upper(),0) for key in mcase})

# 集合推导式

# 计算列表中每个值的平方，自带去重功能
# print({x**2 for x in [-2,2,3]})

