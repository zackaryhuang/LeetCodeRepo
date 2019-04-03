"""
执行用时 : 152 ms, 在Remove Duplicates from Sorted Array的Python提交中击败了21.94% 的用户
内存消耗 : 13.6 MB, 在Remove Duplicates from Sorted Array的Python提交中击败了0.73% 的用户

双指针法
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        time=1
        if(len(nums)==0):
            return 0
        for i in range(0,len(nums)-1):
            if(nums[i]!=nums[i+1]):
                nums[time]=nums[i+1]
                time+=1        
        return time
