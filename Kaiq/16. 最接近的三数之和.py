"""
执行用时 : 136 ms, 在3Sum Closest的Python提交中击败了34.43% 的用户
内存消耗 : 11.7 MB, 在3Sum Closest的Python提交中击败了1.02% 的用户
"""
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        min=nums[0]+nums[1]+nums[2]
        for i in range(0,len(nums)-2):
            l=i+1
            r=len(nums)-1
            while(l<r):
                val = nums[i]+nums[l]+nums[r]
                if(abs(val-target) < abs(min-target)):
                    min=val
                if(val>target):
                    r-=1
                elif(val<target):
                    l+=1
                else:
                    return target
        return min
