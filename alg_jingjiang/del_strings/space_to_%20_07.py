# 先计算一共需要多大的空间，然后从后往前复制

def spaceto20(str):
    str = list(str)
    count = 0
    for i in str:
        if i ==" ":
            str[count] = "%20"
            count += 1
        else:
            count+=1
    return "".join(str)

if __name__ == '__main__':
    str = "I love you"
    b = spaceto20(str)
    print(b)