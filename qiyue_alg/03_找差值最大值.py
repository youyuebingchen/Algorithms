from Getnum import getnum
def maxcha(alist):
    n = len(alist)
    num_min = min(alist)
    num_max = max(alist)
    if num_min == num_max :
        return 0
    d = (num_max-num_min)/(n+1)
    tong = []
    for i in range(n+1):
        tong.insert(i,[])
    print(tong)
    for j in alist:
        if j == num_max:
            tong[n].append(j)
        else:
            index = (j-num_min)*(n+1)//(num_max-num_min)
            tong[index].append(j)
    print(tong)
    temp = []
    for i in range(0,len(tong)):
        if not tong[i] and tong[i-1]:
            for j in range(i,len(tong)):
                if tong[j]:
                    temp.append(min(tong[j]) - max(tong[i-1]))
                    print(temp)
                    break
    return max(temp)


if __name__ == '__main__':
    a = getnum(10)
    maxcha(a)