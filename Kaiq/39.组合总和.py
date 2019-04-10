"""
思路:
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.res=[]
        self.dfs(0,target,candidates,[])
        return self.res
    def dfs(self,index,target,nums,x):
        if(target==0):
            self.res.append(x[:])
            return
        for i in range(index,len(nums)):
            k = target - nums[i]
            if(k>=0):
                # 注意这儿的func（i）而不是func(i+1)，因为可以重用元素，如果是i+1则不重用元素
                self.dfs(i,target-nums[i],nums,x+[nums[i]])
            
