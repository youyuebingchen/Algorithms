# 构建二叉树


# 先构建节点类
class Node(object):
    def __init__(self,item):
        self.elem = item
        self.lchild = None
        self.rchild = None

# 用节点构建二叉树
class BinaryTree(object):
    def __init__(self):
        self.root = None

    #添加元素
    def add(self,item):
        node = Node(item)
        # 判断二叉树是否为空，如果为空直接在根节点添加元素
        if self.root is None:
            self.root = node
            return
        # 构建队列存储和输出节点信息
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            # 对当前节点的左子节点进行处理
            if cur_node.lchild == None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.rchild)
            # 对当前队列的右子节点进行处理
            if cur_node.rchild == None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)
    def spredtravel(self):
        if self.root == None:
            print("空")
            return
        queue = [self.root]

        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem,end=" ")
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    def pre_travel(self,node):
        # node 代表根节点
        if node is None:
            return
        print(node.elem,end=" ")
        self.pre_travel(node.lchild)
        self.pre_travel(node.rchild)
    def mid_travel(self,node):
        if node is None:
            return
        self.mid_travel(node.lchild)
        print(node.elem,end=" ")
        self.mid_travel(node.rchild)

    def last_travel(self,node):
        if node is None:
            return
        self.last_travel(node.lchild)
        self.last_travel(node.rchild)
        print(node.elem, end=" ")


if __name__ == '__main__':
    tree = BinaryTree()
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
    # tree.spredtravel()
    tree.pre_travel(tree.root)
    print("\n")
    tree.mid_travel(tree.root)
    print("\n")
    tree.last_travel(tree.root)