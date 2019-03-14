# 建立节点
class Node(object):
    def __init__(self,item):
        self.elem = item
        self.next = None

class Singlink(object):
    def __init__(self):
        self.head = None
    # 增加元素
    def append(self,item):
        node = Node(item)
        if self.head == None:
            self.head = node
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = node
#遍历
    def travel(self):
        pre = self.head
        while pre is not None:
            print(pre.elem,end=" ")
            pre = pre.next
# 在头部插入元素
    def add(self,item):
        node = Node(item)
        cur = self.head
        self.head = node
        node.next = cur
# 插入元素
    def insert(self,pos,item):
        node = Node(item)
        cur = 1
        pre = self.head
        while cur < pos:
            cur += 1
            pre = pre.next
        node.next = pre.next
        pre.next = node
# 链表删除节点
    def remove(self,item):
        pre = self.head
        cur =pre.next
        while cur.elem != item:
            pre =pre.next
            cur = cur.next
        pre.next = cur.next

# 链表的翻转
    def ele_invert(self):
        pre = self.head
        pcur = pre.next
        #  将pcur一直插到头部即可
        while pcur != None:
            #先将pre.next 指向pcur的下一个node
            pre.next = pcur.next
            # 将pcur 指针指向第一个节点
            pcur.next =self.head
            # 将头结点指向pcur
            self.head = pcur
            # 将pcur 指针重新对准pre.next
            pcur=pre.next





if __name__ == '__main__':
    a = Singlink()
    a.append(4)
    a.append(5)
    a.append(6)
    a.append(7)
    a.insert(1,10)
    a.travel()
    print("\n")
    a.ele_invert()
    a.travel()
    # print("\n")
    # a.remove(6)
    # a.travel()