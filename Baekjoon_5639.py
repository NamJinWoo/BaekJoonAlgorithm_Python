class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.head = Node(None)
        self.postorder_list = []

    def insert(self,num):
        if self.head.key is None:
            self.head.key = num
        else:
            self.insert_node(self.head, num)

    def insert_node(self, node, num):
        if num <= node.key:
            if node.left is not None:
                node.left = self.insert_node(node.left, num)
            else:
                node.left = Node(num)
        else:
            if node.right is not None:
                node.right = self.insert_node(node.right, num)
            else:
                node.right = Node(num)

        return node

    def postorder(self):
        if self.head.key is not None:
            self.postorder_traverse(self.head)

    def postorder_traverse(self, node):
        if node.left is not None:
            self.postorder_traverse(node.left)

        if node.right is not None:
            self.postorder_traverse(node.right)
        print(node.key)


# import sys
bt = BinaryTree()

# n = sys.stdin.read().rstrip()
# l1 = n.split("\n")
# for item in l1:
#     bt.insert(int(item))
# bt.postorder()

while True:
    try:
        key = int(input())
        bt.insert(key)
    except EOFError:
        break
bt.postorder()

