class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1
        if len(nums) == 1:
            if nums[0] > 1:
                return 1
            elif nums[0] == 1:
                return 2
            else:
                return 1
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = 1

        maxNum = max(nums)
        minNum = min(nums)
        if maxNum == minNum and 1 not in nums:
            return 1
        array = [-1] * (maxNum - minNum + 1)
        for num in nums:
            array[num - minNum] = num
        if array[0] != 1:
            return 1
        else:
            for i in range(len(array)):
                if array[i] == -1:
                    return array[i-1] + 1
            return array[len(array) - 1] + 1

if __name__ == "__main__":
    s = Solution()
    print(s.firstMissingPositive([-1,-2]))
            

