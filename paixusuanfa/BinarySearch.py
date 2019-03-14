def BinarySearch(alist,item):
    if item not in alist:
        print("the item not in the list")
    else:
        first = 0
        last = len(alist)-1
        while first <= last:
            mid = (first + last)//2
            if alist[mid] < item:
                first = mid
            elif alist[mid] >item:
                last = mid
            else:
                return mid + 1
test = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(BinarySearch(test, 17))