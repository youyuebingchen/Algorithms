# # bublle sort
# def BubbleSort(array):
#     n = len(array)-1
#     for i in range(n,0,-1):
#         for j in range(i):
#             if array[j] > array[j+1]:
#                 array[j],array[j+1] =  array[j+1],array[j]
#     return array
#
# if __name__ == '__main__':
#     a = [1, 5, 3, 2, 7, 4, 9]
#     b = BubbleSort(a)
#     print(b)


# Selection Sort
# # 选择排序
# def SelectSort(array):
#     n = len(array)-1
#     # print(n)
#     for i in  range(n,-1,-1):
#         # print(i)
#         max = i
#         for j in range(i,-1,-1):
#             if array[max] < array[j]:
#                 max = j
#         array[i] ,array[max] = array[max],array[i]
#     return array

# # 插入排序
# def InsertSort(array):
#     n = len(array)
#     for i in range(1,n):
#         for j in range(i,0,-1):
#             if array[j] < array[j-1]:
#                 array[j],array[j-1] =array[j-1],array[j]
#             else:
#                 break
#     return array



if __name__ == '__main__':
    a = [1,4,2,9,6,5,7,11,16,13,22,10]
    b = InsertSort(a)
    print(b)