def circulmin(alist):
    n = len(alist)
    left = 0
    right = n - 1
    mid = 0
    # 判断左端是否小于右端如果是直接返回左端
    if alist[left] < alist[right]:
        return alist[left]
    if alist[-1] < alist[-2]:
        return alist[-1]
    # 如果不是使用二分查找
    else:
        while left <= right:
            mid = (left + right)//2
            if alist[mid] > alist[mid - 1]:
                right = mid + 1
            else:
                left = mid - 1
            if alist[mid]<alist[mid-1] and alist[mid]<alist[mid+1]:
                return alist[mid]


if __name__ == '__main__':
    a = [4,5,6,7,1,2,3]
    b =circulmin(a)
    print(b)