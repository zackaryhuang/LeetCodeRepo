# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 自顶向下递归,每次加入深度信息
class Solution:
    def Recursion(self, node:TreeNode, outter:List[List[int]], depth:int):
        if len(outter)<depth:
            outter.append([])
        outter[depth-1].append(node.val)
        if node.left:
            self.Recursion(node.left,outter,depth+1)
        if node.right:
            self.Recursion(node.right,outter,depth+1)   
        
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        outter = [[]]
        self.Recursion(root,outter,1)
        #return list(reversed(outter))
        return outter[::-1]
