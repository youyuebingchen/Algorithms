import numpy as np
import re
import pandas as pd
import random
random.ra
def ToLower1(str):
    """
    直接调用lower 的函数
    调用capitalize将首字母由小写变大写
    调用upper()将小写变成大写
    """
    str = str.lower()
    return str

def ToLower2(str):
    """
       大写字母范围：65-90
       小写字母范围：97-122
       两者相差 32
       将字符串转化成List(str)
       将list转化成字符串 ("".join(list))
    """
    a = []
    for i in list(str):
        # ord 获得字符串的ASC码序号
        if ord(i) >= 65 and ord(i) <= 90:
            # chr 将ASC码转化成相应的字符
            b = chr(ord(i) + 32)
            a.append(b)
        else:
            a.append(i)
    return("".join(a))

if __name__ == '__main__':
    str = "Hello"
    b  = ToLower(str)
    print(b)
    b.extern