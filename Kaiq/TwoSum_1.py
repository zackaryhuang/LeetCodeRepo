class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res=[]
        count = len(nums)
        for i in range(0,count):
            for j in range(i+1,count):
                a = target - nums[i];
                if(nums[j] == a):
                    res.append(i)
                    res.append(j)
                    return res
