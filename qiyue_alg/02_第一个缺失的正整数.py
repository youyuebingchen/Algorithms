from Getnum import getnum

def first_loss(alist):
    n = len(alist)
    alist.insert(0,None)
    i = 1
    while i <= n:
        if alist[i] < i or alist[i] >n:
            alist[i] = alist[n]
            n -= 1
        elif alist[i] > i:
            temp = alist[i]
            alist[i] = alist[temp]
            alist[temp] = temp
        else:
            i += 1
    return i





if __name__ == '__main__':
    a = getnum(10)
    print(a)
    b = first_loss(a)
    print(b)