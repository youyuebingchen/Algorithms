import numpy as np


class Queue(object):
    """队列"""
    def __init__(self):
        self.__list = []
    def enqueue(self,item):
        """入队"""
        self.__list.append(item)

    def dequeue(self):
        """出队"""
        return self.__list.pop(0)
    def is_empty(self):
        """判断是否为空"""
        return self.__list == []
    def size(self):
        """返回元素个数"""
        return len(self.__list)

if __name__ == '__main__':
    a = Queue()
    a.enqueue(1)
    a.enqueue(2)
    a.enqueue(3)
    print(a.is_empty())
    print(a.size())
    print(a.dequeue(),end=" ")
    print(a.dequeue(),end=" ")
    print(a.dequeue(),end=" ")
