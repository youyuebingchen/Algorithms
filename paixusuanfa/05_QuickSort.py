import random


def GetNum(n):
    a = []
    while len(a) < n:
        b = random.randint(1, 10*n)
        a.append(b)
    return a



def QuicjSort(alist,first,last):
    """快速排序 重要的考点，面试经常用 """
    n = len(alist)
    if first >= last:
        return
    mid_value = alist[first]
    low = first
    high = last
    while low < high:
        # 包含等于的尽量放在一边
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]
        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
    alist[high] = mid_value
    QuicjSort(alist,first,low-1)
    QuicjSort(alist,low+1,last)
    return alist

if __name__ == '__main__':
    a= GetNum(7)
    print(a)
    print(QuicjSort(a,0,len(a)-1))