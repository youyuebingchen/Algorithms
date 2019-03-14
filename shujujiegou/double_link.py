# 构建节点类
class Node(object):

    def __init__(self,item):
        self.elem = item
        self.lnext = None
        self.rnext = None
class DoubleLink(object):
    """双向联表"""
    def __init__(self):
        self.head = None

    # 在尾部添加元素
    def append(self,item):
        node = Node(item)
        if self.head == None:
            self.head = node
            node.lnext = self.head
            return
        cur = self.head
        while cur.rnext is not None:
            cur = cur.rnext
        cur.rnext = node
        node.lnext = cur
    # 在头部添加元素
    def add(self):
        pass
    # 元素遍历
    def travel(self):
        cur = self.head
        while cur !=None:
            print(cur.elem,end=" ")
            cur = cur.rnext
    # 插入元素
    def inser(self,pos,item):
        node = Node(item)
        count = 0
        cur = self.head
        while count < pos-1:
            cur = cur.rnext
            count += 1
        node.rnext = cur.rnext
        cur.rnext.lnext = node
        cur.rnext = node
        node.lnext = cur
    # 元素翻转
    def elem_invertion(self):
        pass


if __name__ == '__main__':
    a = DoubleLink()
    for i in range(0,10):
        a.append(i)

    a.inser(5,11)
    a.travel()
