class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        lastNum = nums[0]
        idx = 0
        for index in range(1, len(nums)):
            if nums[index] > lastNum:
                lastNum = nums[index]
                idx = index
        if idx != 0:
            minIdx = idx
            minNum = nums[idx]
            for i in range(idx + 1, len(nums[idx:]) + 1):
                if nums[i] < minNum:
                    minNum = nums[i]
                    minIdx = i
            temp = nums[minIdx]
            nums[minIdx] = nums[idx - 1]
            nums[idx - 1] = temp
        else:
            nums.sort()
        return nums
# @lc code=end

s = Solution()
print(s.nextPermutation([1,3,2]))

