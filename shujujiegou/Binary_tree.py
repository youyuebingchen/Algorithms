class Node(object):
    """Node"""
    def __init__(self,item):
        self.elem = item
        self.lchild = None
        self.rchild = None


class Binary_tree(object):
    """二叉树"""
    def __init__(self):
        self.root = None

    def add(self,item):
        node = Node(item)
        # 如果是空树 直接添加
        if self.root is None:
            self.root = node
            return
        # 不是空树的话先进行广度优先遍历找到None节点，然后进行添加
        queue = [self.root]  # 用队列保存要遍历的节点
        # queue.append(self.root)
        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild == None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)

    def breadth_travel(self):
        """广度遍历"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem)
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)
    def pre_travel(self,node):
        """先序遍历：根左右"""
        if node is None:
            return
        print(node.elem,end=" ")
        self.pre_travel(node.lchild)
        self.pre_travel(node.rchild)

    def mid_travel(self,node):
        """中序遍历：左根右"""
        if node is None:
            return
        self.mid_travel(node.lchild)
        print(node.elem, end=" ")
        self.mid_travel(node.rchild)
    def last_travel(self,node):
        """后续遍历：左右根"""
        if node is None:
            return
        self.last_travel(node.lchild)
        self.last_travel(node.rchild)
        print(node.elem,end=" ")


if __name__ == "__main__":
    tree = Binary_tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    print(tree.breadth_travel())
    tree.pre_travel(tree.root)
    print("\r")
    tree.mid_travel(tree.root)
    print("\r")
    tree.last_travel(tree.root)