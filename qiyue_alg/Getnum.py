import random
def getnum(n):
    a = set()
    while len(a) < n:
        b = random.randint(1,10*n)
        a.add(b)
    return list(a)