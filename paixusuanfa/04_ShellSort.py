import random

def GetNum(n):
    a = []
    while len(a) < n:
        b = random.randint(1, 10*n)
        a.append(b)
    return a

def ShellSort(alist):
    """希尔排序"""
    n = len(alist)
    gap = n // 2
    while gap >=1 :
        gap = gap // 2
        # gap //=2
        for j in range(gap,n):
            i = j
            while i > 0 :
                if alist[i] < alist[i-gap]:
                    alist[i],alist[i-gap] = alist[i-gap],alist[i]
                    i -= gap
                else:
                    break
    return alist


if __name__ == '__main__':
    a = GetNum(8)
    print(a)
    print(ShellSort(a))