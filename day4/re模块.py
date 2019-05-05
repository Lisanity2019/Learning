# -*- coding: utf-8 -*-

#----> re模块
#----> 正则表达式
# print(r'\n') #转义问题---->r ===>real

import re
#---->findall
#---->search
#---->match

# ret=re.findall('[a-z]+','ab cd,efg') #---->匹配所有,返回列表
# print(ret)

# ret=re.search('[a-z]+','ab cd,efg')
# print(ret)
# if ret:
#     print(ret.group())   #---->从前往后，找到一个就返回，返回一个对象，需要调用group方法才能拿到结果，如果没有找到返回None,调用group会报错

# ret=re.match('[a-z]+','ab,cd,efg')
# print(ret)
# if ret:
#     print(ret.group())   #---->match从头开始匹配，匹配到返回对象，匹配不到返回None，用法同search

# ret=re.split('[a]','ab acd,efg',4)   #---->分割
# print(ret)

# ret=re.sub('\d','A','3i4gjf3')  #---->替换
# print(ret)

# ret=re.subn('\d','A','3i4gjf3')  #---->传入参数跟sub一样，只是返回替换后的结果 和 替换的次数
# print(ret)

# obj=re.compile('\d')
# print(obj.sub('A','32fd23dfds33'))  #---->将正则表达式编译成对象，然后可以被直接多次重复调用，提高效率。
# 编译后的对象可以使用findall search match sub subn split等方法


