import numpy as np

# 构建堆栈
class stack(object):
    """堆栈"""
    def __init__(self):
        self.__list = []
    def push(self,item):
        """添加一个新元素"""
        self.__list.append(item)
        # print(self.__list)
    def pop(self):
        """弹出一个元素"""
        # print(self.__list)
        return  self.__list.pop()

    def peek(self):
        """返回栈顶元素"""
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty(self):
        """判断堆栈是否为空"""
        return self.__list == []
    def size(self):
        """返回堆栈元素的个数"""
        return len(self.__list)