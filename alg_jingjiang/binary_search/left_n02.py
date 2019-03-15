def left(alist,num):
    n = len(alist)
    left = 0
    right = n-1
    res = -1
    while left <= right:
        mid = (left+right)//2
        if alist[mid] >= num:
            right = mid -1
        elif alist[mid] <= num:
            left = mid+1
        if alist[mid] ==num:
             res = mid
    return res

if __name__ == '__main__':
    a  =[1,2,3,3,3,3,7,4,4,5,6,4]
    b =left(a,4)
    print(b)