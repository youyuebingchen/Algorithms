class TwoSideQueue(object):
    """双端队列"""
    def __init__(self):
        self.__list = []
    def add_front(self,item):
        self.__list.insert(0,item)
    def add_tail(self,item):
        self.__list.append(item)
    def pop_front(self):
        return self.__list.pop(0)
    def pop_tail(self):
        return self.__list.pop()
    def is_empty(self):
        return self.__list == []
    def size(self):
        return len(self.__list)


if __name__ == '__main__':
    a= TwoSideQueue()
    a.add_front(1)
    a.add_tail(2)
    a.add_front(3)
    a.add_tail(4)
    a.add_tail(5)
    for i in range(6):
        print(a.pop_tail())


