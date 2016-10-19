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

    def height(self, root):
        if root == None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1

    def findHeight(self):
        return self.height(self.root)

    def lowestCommonAncestor(self, root, n1, n2):
        if root == None:
            return None

        if root.key < n1 and root.key < n2:
            return self.lowestCommonAncestor(root.right, n1, n2)

        if root.key > n1 and root.key > n2:
            return self.lowestCommonAncestor(root.left, n1, n2)

        return root.key

    def findLowestCommonAncestor(self, n1, n2):
        return self.lowestCommonAncestor(self.root, n1, n2)

if __name__ == '__main__':

    #         10
    #     5       20
    # -1       15     38
    #              31
    #           29
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(20)
    bst.insert(15)
    bst.insert(5)
    bst.insert(-1)
    bst.insert(38)
    bst.insert(31)
    bst.insert(29)

    bst.inorder()
    print('Height : ', bst.findHeight())
    n1 = 31
    n2 = 29
    print('Lowest Common Ancestor (31, 29) : ', bst.findLowestCommonAncestor(n1, n2))
