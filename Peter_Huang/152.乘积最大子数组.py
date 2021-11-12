#
# @lc app=leetcode.cn id=152 lang=python
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        iMax = 0
        iMin = 0
        maxNum = 0
        for idx in range(len(nums)):
            if nums[idx] == 0:
                iMax = 0
                iMin = 0
            if nums[idx] < 0:
                temp = iMax
                iMax = iMin
                iMin = temp
            iMax = max(iMax, (iMax if iMax != 0 else 1) * nums[idx])
            iMin = min(iMin, (iMin if iMin != 0 else 1) * nums[idx])
            maxNum = max(maxNum, iMax)
        return maxNum
# @lc code=end

s = Solution()
print(s.maxProduct([0,4]))


