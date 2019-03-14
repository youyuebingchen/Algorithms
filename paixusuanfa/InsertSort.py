# def InsertSort(alist):
#     n = len(alist)
#     for i in range(1,n-1):
#         for j in range(i,0,-1):
#             if alist[j] < alist[j-1]:
#                 alist[j],alist[j-1] = alist[j-1],alist[j]
#             else:
#                 break
#     return alist
# a = [1,5,3,2,7,4,9]
# b = InsertSort(a)
# print(b)
def InsertSort(array):
    n = len(array)
    for i in range(1,n):
        max = i
        for j in range(i):
            if array[max]<array[j]:
                max = j
        array[i],array[max] = array[max],array[i]
    return array


if __name__ == '__main__':
    a = [1, 5, 3, 2, 7, 4, 9]
    print(InsertSort(a))


