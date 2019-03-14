# https://blog.csdn.net/fuxuemingzhu/article/details/79434100
def single_num(alist):
    temp = 0
    for i in alist:
        temp ^= i
    num1 = 0
    num2 = 0
    mask = 1
    while temp & mask == 0:
        mask <<= 1
        print("mask的值",mask)
        print("二进制mask",bin(mask))
    for num in alist:
        if num & mask == 0:
            num1 ^= num
        else:
            num2 ^= num
    return num1,num2




if __name__ == '__main__':
    a = [ 7,3,4,7,3,4,5,11,9,11,]
    # a = [3,3,4,4,7,7,5,9,11,11]
    c,d =single_num(a)
    print(c,d)