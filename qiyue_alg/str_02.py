# 删除一个字符串所有的a,并复制所有的b
def str_remove(str):
    n = len(str)
    count = 0
    i = 0
    j = 0
    while i < len(str):
        if str[i] == "a":
            str= str[:i] + str[i+1:]
            i -=1
        i +=1

    while j < len(str):
        if str[j] =="b":
            count +=1
        j +=1
    return  str,count

# 节省了空间但是改变了原来数组的顺序
def str_remove_array(str):
    str = list(str)
    i = 0
    j = 0
    count = 0
    while  i <len(str):
        if str[i] == "a":
            str[i]=str[-1]
            str.pop()
            i -=1
        i +=1
    while j <len(str):
        if str[j] =="b":
            count +=1
        j +=1
    return "".join(str),count

def space(str):
    i = 0
    while i < len(str):
        if str[i] ==" ":
            str = str[:i] +"%20"+str[i+1:]
            i -=1
        i+=1
    return str
if __name__ == '__main__':
    a = " b cdefagabdb "
    # str,count = str_remove_array(a)
    # print(str)
    # print(count)
    b = space(a)
    print(b)