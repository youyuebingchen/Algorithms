def QuickSort(alist):
    qsort_rec(alist,0,len(alist)-1)
    return alist

def qsort_rec(alist,l,r):
    if l > r:
        return
    i = l
    j = r
    mid = alist[i]

    while i < j :
        while i < j and alist[j] >= mid:
            j -= 1
        if i < j:
            alist[i] = alist[j]
            i += 1
        while i < j and alist[i] <= mid:
            i += 1
        if i < j:
            alist[j] = alist[i]
            j -= 1
        alist[i] = mid
        qsort_rec(alist,l,i-1)
        qsort_rec(alist,i+1,r)

test = [1, 5, 3, 2, 7, 4, 9]
print(QuickSort(test))