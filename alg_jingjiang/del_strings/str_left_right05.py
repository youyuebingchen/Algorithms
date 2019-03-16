def invert(str):
    str = list(str)
    n  = len(str)
    left = 0
    right = n - 1
    while left <= right:
        str[left],str[right] = str[right],str[left]
        left+=1
        right-=1
    return "".join(str)
if __name__ == '__main__':
    str = "I love you , do you love me ? "
    b = invert(str)
    print(b)
    c = []
    for i in b.split(sep=" "):
        d = invert(i)
        c.append(d)
    print(" ".join(c))