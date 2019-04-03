

"""
执行用时 : 296 ms, 在Find First and Last Position of Element in Sorted Array的Python提交中击败了0.89% 的用户
内存消耗 : 13.6 MB, 在Find First and Last Position of Element in Sorted Array的Python提交中击败了0.00% 的用户
"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        count=0
        for i in range(0,len(nums)):
            if(nums[i]==target):
                count+=1
            if(count>0 and nums[i]!=target):
                return i-count,i-1
            if(count>0 and i==len(nums)-1):
                return [i-count+1,i]
        return [-1,-1]
