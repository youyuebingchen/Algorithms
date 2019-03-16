# def a function to do inverse all the string
def inverse(str):
    str = list(str)
    n = len(str)
    left = 0
    right = n-1
    while left <= right:
        str[left],str[right] = str[right],str[left]
        left += 1
        right -= 1
    return "".join(str)


if __name__ == '__main__':
    a = " i love you"
    b = inverse(a)
    print(b)
    d = []
    for i in b.split(sep=" "):
        c = inverse(i)
        d.append(c)
    print(" ".join(d))