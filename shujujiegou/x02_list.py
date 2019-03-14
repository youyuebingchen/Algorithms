from timeit import Timer
li1 = [1,2]
li2 = [3,4]
li = li1 + li2



def test1():
    li = []
    for i in range(10000):
        li.append(i)


def test2():
    li = []
    for i in range(10000):
        li+=[i]


def test3():
    li = [i for i in range(10000)]



def test4():
    li = list(range(10000))



if __name__ == '__main__':
    time1 = Timer("test1()","from __main__ import test1")
    t1 = time1.timeit(1000)
    time2 = Timer("test2()","from __main__ import test2")
    t2 = time2.timeit(1000)
    time3 = Timer("test3()","from __main__ import test3")
    t3 = time3.timeit(1000)
    time4 = Timer("test4()","from __main__ import test4")
    t4 = time4.timeit(1000)
    print(t1)
    print(t2)
    print(t3)
    print(t4)



