def socal(alist):
    """求哪个玩家分数最高时多少"""
    n = len(alist)
    scoal_a = 0
    scoal_b = 0
    while n> 0:
        mid = max(alist[0],alist[-1])
        scoal_a +=  mid
        alist.remove(mid)
        n-=1
        if n == 0:
            break
        mid = max(alist[0], alist[-1])
        scoal_b = mid = max(alist[0], alist[-1])
        alist.remove(mid)
        n -= 1
    return scoal_a,scoal_b
a = [1,4,3, 5, 3, 2, 7, 4, 9]
b,c = socal(a)
print(b,c)


