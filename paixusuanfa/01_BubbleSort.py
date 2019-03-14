import numpy as np
import random
def GetNum(n):
    a = []
    while len(a) < n:
        b = random.randint(1, 10*n)
        a.append(b)
    return a
def Bubblesort(alist):
    """冒泡排序"""
    n = len(alist) - 1
    # i代表下标
    for i in range(n):
        count = 0
        for j in range(n-i):
            if alist[j] >alist[j+1]:
                alist[j],alist[j+1] = alist[j+1],alist[j]
                count += 1
        if count == 0:
            break
    return alist
if __name__ == '__main__':
    a =GetNum(7)
    print(a)
    print(Bubblesort(a))
