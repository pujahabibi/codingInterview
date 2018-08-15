class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)

        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)

        else:
            print("the value is already present in the tree")

    def find(self, data):
        if self.root:
            is_found = self._find(data, self.root)
            if is_found:
                return True
            else:
                return False
        else:
            return None

    def _find(self, data, cur_node):
        if data > cur_node.data and cur_node.right: #check if cur_node.right exist
            return self._find(data, cur_node.right)
        elif data < cur_node.data and cur_node.left:
            return self._find(data, cur_node.left)
        if data == cur_node.data:
            return True
        else:
            return False

    def inorder_print(self):
        if self.root:
            self._inorder_print(self.root)

    def _inorder_print(self, cur_node):
        if cur_node:
            self._inorder_print(cur_node.left)
            print(str(cur_node.data))
            self._inorder_print(cur_node.right)

    def is_bst(self):
        if self.root:
            is_satisfied = self._is_bst(self.root, self.root.data)
            if is_satisfied is None:
                return True
            return False

    def _is_bst(self, cur_node, data):
        if cur_node.left:
            if data > cur_node.left.data:
                return self._is_bst(cur_node.left, cur_node.left.data)
            else:
                return False
        if cur_node.right:
            if data < cur_node.right.data:
                return self._is_bst(cur_node.right, cur_node.data)
            else:
                return False


bst = BST()
bst.insert(4)
bst.insert(2)
bst.insert(8)
bst.insert(5)
bst.insert(10)


tree = BST()
x = BST()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
print(tree.is_bst())
print(bst.is_bst())
print(x.is_bst())