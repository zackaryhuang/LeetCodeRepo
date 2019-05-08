# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#list中间数做root,左右两边递归
class Solution:
    def Recursion(self, nums: List[int], start: int, end: int) -> TreeNode:
        if start > end:
            return None
        elif start == end:
            return TreeNode(nums[start])
        else:
            mid = (start + end) // 2
            node = TreeNode(nums[mid])
            node.left = self.Recursion(nums, start, mid - 1)
            node.right = self.Recursion(nums, mid + 1, end)
            return node
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.Recursion(nums, 0, len(nums) - 1)
    
    
