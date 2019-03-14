import random

def GetNum(n):
    a = []
    while len(a) < n:
        b = random.randint(1, 10*n)
        a.append(b)
    return a


def Binary_search(alist,item):
    """在排序算法(递归版本)的基础上进行二分查找"""
    n = len(alist)
    if n > 0:
        mid = n // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return Binary_search(alist[:mid],item)
        else:
            return Binary_search(alist[mid+1:],item)
    return False

def Binary_search2(alist,item):
    n = len(alist)
    first = 0
    last = n - 1
    while first <= last:
        mid = (first+last)//2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            last = mid - 1
        else:
            first =mid + 1
    return False

if __name__ == '__main__':
    a = [2, 3, 4, 30, 46, 49, 56]
    print(a)
    print(Binary_search2(a,46))
