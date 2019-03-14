from Getnum import getnum

def sum(alist):
    b = []
    n = len(alist)
    temp = 0
    for i in range(n):
        temp += alist[i]
        b.append(temp)
    return b
if __name__ == '__main__':
    # a = getnum(10)
    a = [1,2,3,4,5,6,7,8,9]
    b = sum(a)
    print(b)
    print(b[3]-b[1])