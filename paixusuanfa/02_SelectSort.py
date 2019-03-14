import numpy as np
import random
def GetNum(n):
    a = []
    while len(a) < n:
        b = random.randint(1, 10*n)
        a.append(b)
    return a

def SelectSort(alist):
    """选择排序"""
    n = len(alist) - 1
    for i in range(n):
        min_index = i
        count = 0
        for j in range(i+1,n+1):
            if alist[min_index] > alist[j]:
                min_index = j
                count += 1
        alist[i],alist[min_index] = alist[min_index],alist[i]
        if count == 0 :
            break
    return alist


if __name__ == '__main__':
    a = GetNum(7)
    print(a)
    print(SelectSort(a))
