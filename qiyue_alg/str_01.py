# 把一个 0-1串进行排序，可以任意交换两个位置，问最少交换的次数



def main(alist):
    n = len(alist)
    left = 0
    right = n-1
    mid = 0
    while left <=right:
        while left <= right and alist[left] == 1:
            while left <= right and alist[right] == 0:
                alist[left],alist[right] = alist[right],alist[left]
            right -=1
        left +=1
    return alist


if __name__ == '__main__':
    a = [1,0,0,1,0,1,0,1,0,1,0,0]
    list = main(a)
    print(list)