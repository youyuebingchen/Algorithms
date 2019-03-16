# 如果一个字符串，吧字符串前面任意的部分木偶东到后面去
# 形成的字符串叫做str的旋转词。给定两个字符串a和b，请判断a 和 b是否互为旋转词
def scraw(str1,str2):
    str = str1+str1
    print(str)
    n = len(str)
    crop = []
    for i in range(1,n-4):
        v = str[i:i+4]
        crop.append(v)
    print(crop)
    if str2 in crop:
        return "YES"
    else:
        return "NO"
# KMP算法：从头到尾匹配，一旦不匹配指针回到开始下移一位
def scraw2(str1,str2):
    str = str1+str1
    i = 0
    j = 0
    start = 0
    if len(str1) != len(str2):
        return "no"
    while i < len(str) and j <len(str2):
        if str[i] == str2[j]:
            i += 1
            j +=1
        else:
            start +=1
            i = start # i - j + 1
            j = 0
    if j == len(str2):
        return "yes"
    else:
        return "no"
if __name__ == '__main__':
    str1 = "abcd"
    str2 = "cdab"
    print(scraw2(str1,str2))