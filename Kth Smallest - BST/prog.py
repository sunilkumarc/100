# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    inorder = []
    
    def inOrderTraversal(self, root):
        if root:
            self.inOrderTraversal(root.left)
            Solution.inorder.append(root.val)
            self.inOrderTraversal(root.right)
            
    def kthSmallest(self, root, k):
        Solution.inorder = []
        self.inOrderTraversal(root)
        
        print(Solution.inorder)
        return Solution.inorder[k-1]
        