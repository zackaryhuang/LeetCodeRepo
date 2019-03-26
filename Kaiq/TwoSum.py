class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res=[]
        count = len(nums)
        for i in range(0,count):
            a = target - nums[i];
            if a in nums[i+1:]:
                return [i,nums.index(a,i+1)] #index(value,start,end)
