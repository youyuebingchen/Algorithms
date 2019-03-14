# 子串变位词


def change(a,b):
    m = len(a)
    n = len(b)
    i = 0
    if n >m:
        return False
    while i+n<=m:
        if a[i:i+n] ==b:
            return True
        i+=1
    return False


if __name__ == '__main__':
    a = "hdfsdfadfadello"
    b = "aell"
    print(change(a,b))
