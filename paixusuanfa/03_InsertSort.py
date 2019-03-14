import  random

def GetNum(n):
    a = []
    while len(a) < n:
        b = random.randint(1, 10*n)
        a.append(b)
    return a

def InsertSort(alist):
    """插入排序"""
    n = len(alist)
    for i in range(1,n):
        for j in range(i,0,-1):
            if alist[j] < alist[j-1]:
                alist[j],alist[j-1] = alist[j-1],alist[j]
            else:
                break
    return alist


if __name__ == '__main__':
    a= GetNum(7)
    print(a)
    print(InsertSort(a))