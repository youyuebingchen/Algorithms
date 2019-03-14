import random
def getnum(n):
    a = set()
    while len(a) < n:
        b = random.randint(1,10*n)
        a.add(b)
    return list(a)
def min(alist):
    if alist == []:
        return -1
    elif len(alist)==1:
        return alist[0]
    elif alist[0] < alist[1]:
        return alist[0]
    elif alist[-1] < alist[-2]:
        return alist[-1]
    left = 1
    right = len(alist)-2
    mid = 0
    while left < right:
        mid = (left+right)//2
        if alist[mid] >alist[mid-1]:
            right = mid - 1
        elif alist[mid] > alist[mid+1]:
            left = mid +1
        else:
            return alist[mid]
    return alist[left]

if __name__ == '__main__':
    alist = getnum(10)
    print(alist)
    b = min(alist)
    print(b)