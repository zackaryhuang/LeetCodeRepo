# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def Recursion(self,node,depth,flag):
        if node == None:
            return depth
        else:
            l=self.Recursion(node.left,depth,flag)
            r=self.Recursion(node.right,depth,flag)
            if abs(l-r)>1:
                flag[0]='F'            
            return 1+max(l,r)
    def isBalanced(self, root: TreeNode) -> bool:
        is_true=['T']
        self.Recursion(root,1,is_true)
        if is_true[0] == 'F':
            return False
        else:
            return True
       
        
