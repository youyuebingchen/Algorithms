import numpy as np


class Node(object):
    """节点"""
    def __init__(self,elem):
        self.elem = elem
        self.next = None


class Singlelink(object):
    """singlelink"""
    def __init__(self,node=None):
        self._head = node

    def is_empty(self):
        """判断链表是否为空"""
        return self._head == None

    def length(self):
        """返回链表的长度"""
        # 空链表的情况
        # 指针情况
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表元素"""
        cur = self._head
        while cur != None:
            print(cur.elem,end=" ")
            cur = cur.next

    def add(self,item):
        """在头部添加元素"""
        node = Node(item)
        node.next = self._head
        self._head = node

    def append(self,item):
        """在尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self._head =node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self,pos,item):
        """在指定位置添加元素"""
        node = Node(item)
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            pre =self._head
            count = 0
            while count < (pos-1):
                count +=1
                pre =pre.next
            node.next =pre.next
            pre.next = node

    def remove(self,item):
        """删除节点"""
        cur =self._head
        pre = None
        while cur != None:
            if cur.elem == item:
                pre.next =cur.next
            else:
                pre =cur
                cur =cur.next
            break

    def search(self,item):
        """查找节点是否存在"""
        cur = self._head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

if __name__ == '__main__':
    ll = Singlelink()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.add(8)

    ll.insert(3,11)
    print(ll.is_empty())
    print(ll.length())
    ll.travel()
    print(ll.search(11))