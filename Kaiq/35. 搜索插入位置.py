"""
执行用时 : 108 ms, 在Search Insert Position的Python提交中击败了0.84% 的用户
内存消耗 : 12.3 MB, 在Search Insert Position的Python提交中击败了0.76% 的用户
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in nums:
            if(i>=target):
                return nums.index(i)
        return len(nums)

