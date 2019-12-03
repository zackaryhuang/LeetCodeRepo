class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = [nums[0],0]
        for i in range(1, len(nums)):
            if nums[i] > a[1]:
                a[2] = nums[i]
            else:
                a[1] = nums[i]

