# https://blog.csdn.net/z983002710/article/details/81164777
# 摩尔投票方法
def find_num(alist):
    n = len(alist)
    count = 0
    for i in range(0,n):
        if count == 0:
            number = alist[i]
            count = 1
        elif number != alist[i]:
            count -=1
        else:
            count +=1
    return number





if __name__ == '__main__':
    a = [4,4,5,2,1,3,3,3,3,3,3]
    b = find_num(a)
    print(b)