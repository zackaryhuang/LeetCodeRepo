class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(0, len(nums)):
            if target == nums[i]:
                return i
            elif target < nums[i]:
                return i
        return len(nums)
if __name__ == "__main__":
    s = Solution()
    res = s.searchInsert([1,3,5,6], 0) 
    print(res)
        
