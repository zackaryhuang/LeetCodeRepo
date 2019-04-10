"""
思路:从后往前找到第一个个大的数
    然后把后面的数中比第一个数大的最小值和这个数交换
    对交换后的后面的数进行升序排序
"""


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=len(nums)-2
        while(i>=0 and nums[i+1]<=nums[i]):
            i-=1
        if(i>=0):
            j=len(nums)-1
            while(j>=i and nums[j]<=nums[i]):
                j-=1
            self.swap(nums,i,j)
        self.reverse(nums,i+1)
        
    def reverse(self, nums,start):
        i = start
        j = len(nums) - 1
        while i < j :
            self.swap(nums,i,j)
            i += 1
            j -= 1         
            
    def swap(self,nums,i,j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

            
