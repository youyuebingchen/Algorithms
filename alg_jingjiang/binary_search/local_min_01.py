def localmin(alist):
    first = 0
    n = len(alist)
    last = n -1
    # 判断是否为空如果为空返回Fasle
    if n == 0:
        return False
    # 判断是否为1如果为1直接返回0
    if n == 1:
        return 1
    # 长度大于1则直接判断两边的大小关系
    if alist[0] < alist[1]:
        return 1
    elif alist[-1] < alist[-2]:
        return n
    # 如果两边都比较大，则取中间进行二分比较
    while first <= last:
        mid = (first + last) // 2
        if alist[mid] > alist[mid - 1]:
            last=mid - 1
        elif alist[mid] > alist[mid + 1]:
            first=mid + 1
        else:
            return mid + 1

if __name__ == '__main__':
    alist = [7,5,2,1,3,7,8,9]
    n = len(alist)
    a = localmin(alist)
    print(a)