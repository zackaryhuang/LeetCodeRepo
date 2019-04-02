"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换

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
