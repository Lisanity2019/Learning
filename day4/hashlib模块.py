# -*- coding: utf-8 -*-

import hashlib

# ----> 摘要算法
md5 = hashlib.md5()
md5.update(b'alex001')
print(md5.hexdigest())

# 摘要算法应用：
# ----> 密码的密文存储
# ----> 文件的一致性验证
