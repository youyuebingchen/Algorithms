import  random

def GetNum(n):
    a = []
    while n > 0 :
        b = random.randint(0,10*n)
        a.append(b)
        n -= 1
    return a

def Merge_Sort(alist):
    n = len(alist)
    if n <= 1:
        return alist
    mid_index = n//2
    left_list = Merge_Sort(alist[:mid_index])
    right_list = Merge_Sort(alist[mid_index:])
    left_point = 0
    right_point = 0
    result = []

    while left_point < len(left_list) and right_point < len(right_list):
        if left_list[left_point] <= right_list[right_point]:
            result.append(left_list[left_point])
            left_point +=1
        else:
            result.append(right_list[right_point])
            right_point += 1
    result += left_list[left_point:]
    result += right_list[right_point:]
    return result


if __name__ == '__main__':
    a= GetNum(7)
    print(a)
    print(Merge_Sort(a))

