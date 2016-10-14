class Node():
    def __init__(self, val):
        self.left = None
        self.right = None
        self.key = val

class BinarySearchTree():
    def __init__(self):
        self.root = None

    def insertNode(self, root, val):
        if root is None:
            root = Node(val)
        else:
            if val < root.key:
                root.left = self.insertNode(root.left, val)
            else:
                root.right = self.insertNode(root.right, val)

        return root

    def inorderTraversal(self, root):
        if root:
            self.inorderTraversal(root.left)
            print(root.key)
            self.inorderTraversal(root.right)

    def inorder(self):
        self.inorderTraversal(self.root)

    def insert(self, val):
        self.root = self.insertNode(self.root, val)

if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(20)
    bst.insert(5)
    bst.insert(-1)
    bst.insert(38)
    bst.insert(31)

    bst.inorder()
