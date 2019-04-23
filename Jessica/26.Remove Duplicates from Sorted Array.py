class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new=list(set(nums))
        new.sort(key=nums.index)
        for i in range(0,len(new)):
            nums[i]=new[i]        
        return len(new)
