class Node():
    def __init__(self, val):
        self.key = val
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self):
        self.root = None

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

    def lowestCommonAncestor(self, n1, n2):
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
    print('Lowest Common Ancestor - method1 (5, 6)', bt.lowestCommonAncestor(6, 8))
