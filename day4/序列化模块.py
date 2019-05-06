# -*- coding: utf-8 -*-

# ----> 序列化:将原本的字典、列表等内容转换成一个字符串的过程 反序列化：---
# ----> 序列化的目的：
# ----> 1.以某种存储形式使自定义对象持久化
# ----> 2.将对象从一个地方传递到另一个地方
# ----> 3.使程序更具维护性

# ---->json    *****  通用的序列化格式
# ---->pickle   ****  所有python中的数据类型都可以转换成字符串形式，序列化内容只有python能理解，且反序列化依赖代码


# ---->json dumps序列化  loads反序列化 在内存中操作
import json

# dic={'k1':'v1'}
# print(dic)
# str_d=json.dumps(dic) #---->序列化
# print(str_d,type(str_d))
# dic_d=json.loads(str_d) #---->反序列化
# print(dic_d)

# ---->json dump序列化  load反序列化  在文件中操作
# dic = {'k1': '中'}
# with open('abc.txt','a',encoding='utf-8')as f:   #---->序列化
#     json.dump(dic,f,ensure_ascii=False)
# with open('abc.txt', 'r', encoding='utf-8')as f: #---->反序列化
#    ret=json.load(f)
# print(ret,type(ret))