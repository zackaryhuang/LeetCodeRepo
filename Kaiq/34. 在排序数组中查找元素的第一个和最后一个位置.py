

"""
执行用时 : 296 ms, 在Find First and Last Position of Element in Sorted Array的Python提交中击败了0.89% 的用户
内存消耗 : 13.6 MB, 在Find First and Last Position of Element in Sorted Array的Python提交中击败了0.00% 的用户
1. 第一个版本时间复杂度为O(n),没注意到题目要求的O(logN)
2. 第二个版本符合题目要求 两个二分  第一个找到左边边界  第二个找到右边边界
"""




##Version.1
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

##Version.2
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        5 7 7 8 8 10 
        """
        if(len(nums)==0):
            return [-1,-1]
        left=0
        right=len(nums)-1
        res=[]
        ##先找左边 
        while(left<right):
            mid = (left+right)/2
            if(nums[mid] < target):
                left = mid+1
            else:
                right = mid
        if(nums[left]!=target):
            return [-1,-1]
        else:
            res.append(left)
        right=len(nums)-1 
        
        ##再找右边
        while(left<right):
            mid=(left+right+1)/2
            if(nums[mid]<=target):
                left=mid
            else:
                right=mid-1
        res.append(right)
        return res
