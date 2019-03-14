# def SelectSort(alist):
#     n = len(alist)
#     for i in range(n-1):
#         min = i
#         for j in range(n-i):
#             if alist[min] > alist[i+j]:
#                 min = i+j
#         alist[i],alist[min] = alist[min],alist[i]
#     return alist
# a = [1, 5, 3, 2, 7, 4, 9]
# b = SelectSort(a)
# print(b)


def SelectSort(array):
    n = len(array)
    for i in range(n):
        min = i
        for j in range(n-i):
            if array[min]> array[i+j]:
                min = i+j
        array[min],array[i] = array[i],array[min]
    return array
if __name__ == '__main__':
    a = [1, 5, 3, 2, 7, 4, 9]
    print(SelectSort(a))