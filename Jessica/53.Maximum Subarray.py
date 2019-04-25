class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        MaxSum=nums[0]
        for i in range(1,len(nums)):
            if nums[i-1]>0:
                nums[i]+=nums[i-1]
            else:
                nums[i]+=0
            if nums[i]>MaxSum:
                MaxSum=nums[i]
        return MaxSum
                
            
        
