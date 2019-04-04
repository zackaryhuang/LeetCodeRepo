"""
二分查找

O(logn)
"""


def search1(nums,start,end,target):
    if(start>end):
        return -1
    mid = (start+end)/2
    if(nums[mid]==target):
        return mid
    if(nums[mid]<nums[end]):
        if(nums[mid]<target and target <=nums[end]):
            return search1(nums,mid+1,end,target)
        else:
            return search1(nums,start,mid-1,target)
    else:
        if(nums[mid]>target and target >=nums[start]):
            return search1(nums,start,mid-1,target)
        else:
            return search1(nums,mid+1,end,target)

class Solution(object):
    
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        return search1(nums,0,len(nums)-1,target)
