# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.Recursion(root.left,root.right)
    def Recursion(self,n1,n2):
        if n1 is None and n2 is None:
            return True
        elif n1 is None or n2 is None:
            return False
        elif n1.val != n2.val:
            return False
        else:
            return self.Recursion(n1.left,n2.right) and self.Recursion(n1.right,n2.left)
        
       
