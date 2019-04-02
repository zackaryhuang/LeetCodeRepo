"""
执行用时 : 60 ms, 在Remove Element的Python提交中击败了0.84% 的用户
内存消耗 : 11.7 MB, 在Remove Element的Python提交中击败了0.54% 的用户
List.remoove
"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            nums.remove(val)
        return len(nums)
