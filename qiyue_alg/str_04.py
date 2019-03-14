# 单词翻转

def inplace(str):
    str = list(str)
    n = len(str)
    i = 0
    j = n-1
    while i < j:
        str[i],str[j] = str[j],str[i]
        i +=1
        j -=1
    return "".join(str)
def inversion(str):
    mid = []
    # str =str[::-1]
    str = inplace(str)
    print(str)
    str = str.split(" ")
    for i in str:
        # a = i[::-1]
        a = inplace(i)
        print(a)
        mid.append(a)
    return " ".join(mid)


if __name__ == '__main__':
    a = "I love you too "
    b = inversion(a)
    print(b)
    # b = inplace(a)
    # print(b)