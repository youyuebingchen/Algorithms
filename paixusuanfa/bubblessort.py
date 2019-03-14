# def BubbuleSort(alist):
#     n = len(alist)-1
#     exchange = True
#     while n >=1 and exchange:
#         exchange = False
#         for j in range(n):
#             if alist[j] > alist[j+1]:
#                 alist[j],alist[j+1] = alist[j+1],alist[j]
#                 exchange = True
#         n-=1
#     return alist

# a = [1,3,2,7,4,5,9]
# b = BubbuleSort(a)
# print(b)

def BublleSort(array):
    n = len(array)
    for i in range(n-1,0,-1):
        # print(i)
        for j in range(i):
            # print(j)
            if array[j]>array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]

    return array

if __name__ == "__main__":
	a = [1,4,2,9,6,5,7,11,16,13,10,22]
	print(BublleSort(a))

