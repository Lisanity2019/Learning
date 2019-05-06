# -*- coding: utf-8 -*-

import random
# print(random.randint(1,2)) #----> 产生一个指定范围内的随机整数，包括尾部，不支持步长
# print(random.random())  #----> 产生一个(0，1)之间的小数不包括0，1
# print(random.randrange(1,10,2)) #----> 产生一个>=1且<10的奇数 可以指定步长
# print(random.choice([1,2,3,4,5]))  #----> 随机选择一个返回
# print(random.sample([1,2,3,4],3))  #----> 随机选择多个返回，返回的是一个列表
# ls=[1,2,3,4,5]
# random.shuffle(ls)  #----> 打乱次序 支持带索引的序列，不支持元组
# print(ls)

#----> 生成随机验证码
# random_number_str=''
# for i in range(10):
#     random_number_str+=str(random.randint(0,9))
# print(random_number_str)