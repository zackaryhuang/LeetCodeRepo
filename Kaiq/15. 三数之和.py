"""
执行用时 : 728 ms, 在3Sum的Python提交中击败了74.81% 的用户
内存消耗 : 15.2 MB, 在3Sum的Python提交中击败了3.45% 的用户

双指针法
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()          
        ans=[]
        for k in range(0,len(nums)):
            if(k==0 or nums[k]>nums[k-1]):
                i=k+1
                j=len(nums)-1
                while(i<j):
                    s=nums[i]+nums[k]+nums[j]
                    if(s==0):
                            ans.append([nums[k],nums[i],nums[j]])
                            i+=1
                            j-=1
                            while(i<j and nums[i]==nums[i-1]):
                                i+=1
                            while(i<j and nums[j]==nums[j+1]):
                                j-=1
                    elif(s<0):
                            i+=1
                    else:
                            j-=1
        return ans
