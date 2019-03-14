# 希尔排序

# def ShellSort(array):
#     n = len(array)
#     tem = 0
#     gap = 1
#     while (gap < n/3):
#         gap = gap*2 + 1
#         print(gap)
#     for i in [for o in gap//3]:
#

def gapInsertionSort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        currentValue = alist[i]
        position = i

        while position >= gap and alist[position-gap] > currentValue:
            alist[position] = alist[position-gap]
            position = position-gap
        alist[position] = currentValue

if __name__ == '__main__':
    a = [1,4,2,9,6,5,7]
    gapInsertionSort(a,0,1)