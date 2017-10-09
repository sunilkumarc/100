# https://leetcode.com/problems/subtree-of-another-tree/description/

# Solution:
# Postorder traversal of second tree should be present in postorder 
# traversal of first tree

# or

# Inorder and Preorder traversal of second tree should be equal to
# respective traversls of tree one

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    postOrder = []
    
    def postOrderTraversal(self, root):
        if root:
            self.postOrderTraversal(root.left)
            self.postOrderTraversal(root.right)
            Solution.postOrder.append('-' + str(root.val) + '-')
        else:
            Solution.postOrder.append('#')
    
    def areIdentical(self, s, t):
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        
        return s.val == t.val and self.areIdentical(s.left, t.left) and self.areIdentical(s.right, t.right)
        
    def isSubtree(self, s, t):
#         if t is None:
#             return True
        
#         if s is None:
#             return False
        
#         if self.areIdentical(s, t):
#             return True
        
#         return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        Solution.postOrder = []
        self.postOrderTraversal(s)
        arr1 = Solution.postOrder
        
        Solution.postOrder = []
        self.postOrderTraversal(t)
        arr2 = Solution.postOrder
        
        arr1 = ''.join(arr1)
        arr2 = ''.join(arr2)
        
        print(arr1, arr2)
        res = arr1.find(arr2)
        
        if res != -1:
            
            return True
        
        return False
        