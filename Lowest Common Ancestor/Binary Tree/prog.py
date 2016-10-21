# Implementation based on the below source
# http://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/

class Node():
    def __init__(self, val):
        self.key = val
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self):
        self.root = None
        self.n1Present = False
        self.n2Present = False

    def insert(self, arr):
        self.root = Node(arr[0])
        self.root.left = Node(arr[1])
        self.root.right = Node(arr[2])
        self.root.left.left = Node(arr[3])
        self.root.left.right = Node(arr[4])
        self.root.right.left = Node(arr[5])
        self.root.right.right = Node(arr[6])
        self.root.right.left.left = Node(arr[7])

    def inorder(self, root):
        if root != None:
            self.inorder(root.left)
            print(root.key)
            self.inorder(root.right)

    def inorderTraversal(self):
        self.inorder(self.root)

    def findPath(self, root, path, n):
        if root == None:
            return path, False

        path.append(root.key)

        # print('Looking in :', root.key)
        if root.key == n:
            return path, True

        if root.left != None:
            path, nPresentInLeft = self.findPath(root.left, path, n)
            if nPresentInLeft == True:
                return path, True

        if root.right != None:
            path, nPresentInRight = self.findPath(root.right, path, n)
            if nPresentInRight == True:
                return path, True

        path.pop()
        return path, False

    def lowestCommonAncestor1(self, n1, n2):
        path1 = []
        path2 = []
        path1, n1Present = self.findPath(self.root, path1, n1)
        path2, n2Present = self.findPath(self.root, path2, n2)

        if not n1Present or not n2Present:
            return -1

        i = 1
        for i in range(min(len(path1), len(path2))):
            if path1[i] != path2[i]:
                return path1[i-1]

        return path1[min(len(path1), len(path2))-1]

    def lowestCommonAncestor2Utility(self, root, n1, n2):
        if root == None:
            return None

        if root.key == n1 or root.key == n2:
            return root.key

        leftLCA = self.lowestCommonAncestor2Utility(root.left, n1, n2)
        rightLCA = self.lowestCommonAncestor2Utility(root.right, n1, n2)

        if leftLCA != None and rightLCA != None:
            return root.key

        if leftLCA != None:
            return leftLCA
        return rightLCA

    def lowestCommonAncestor2(self, n1, n2):
        return self.lowestCommonAncestor2Utility(self.root, n1, n2)

    def lowestCommonAncestor3Utility(self, root, n1, n2):
        if root == None:
            return None

        if root.key == n1:
            self.n1Present = True
            return root
        if root.key == n2:
            self.n2Present = True
            return root

        leftLCA = self.lowestCommonAncestor3Utility(root.left, n1, n2)
        rightLCA = self.lowestCommonAncestor3Utility(root.right, n1, n2)

        if leftLCA != None and rightLCA != None:
            return root

        if leftLCA != None:
            return leftLCA

        return rightLCA

    def findTheOther(self, root, n):
        if root == None:
            return False

        if (root.key == n) or (self.findTheOther(root.left, n)) or (self.findTheOther(root.right, n)):
            return True

        return False

    def lowestCommonAncestor3(self, n1, n2):
        n1Present = False
        n2Present = False

        lca = self.lowestCommonAncestor3Utility(self.root, n1, n2)
        if ((self.n1Present and self.n2Present) or (self.n1Present and self.findTheOther(lca, n2)) or (self.n2Present and self.findTheOther(lca, n1))):
            return lca.key
        return None

if __name__ == '__main__':
    bt = BinaryTree()
    values = [1, 2, 3, 4, 5, 6, 7, 8]
    bt.insert(values)
    bt.inorderTraversal()

    #         1
    #     2       3
    # 4       5 6     7
    #         8

    # First way
    # Create two arrays with paths from root to n1 and root to n2
    # Then traverse through both the arrays until you find first non equal element and return the previous element
    print('Lowest Common Ancestor using Vector Array - ', bt.lowestCommonAncestor1(4, 7))

    # Second way
    # Assuming both the elements are present in the tree
    print('Lowest Common Ancestor assuming both keys exist - ', bt.lowestCommonAncestor2(4, 7))

    # Third way
    # Similar to second one. But doesn't assume both the keys are present in the tree
    print('Lowest Common Ancestor with no assumptions - ', bt.lowestCommonAncestor3(4, 7))
