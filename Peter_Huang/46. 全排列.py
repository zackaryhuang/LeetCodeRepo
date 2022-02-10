class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = self.recursion(nums)
        return res
    

    def recursion(self, nums):
        if len(nums) == 1:
            return [[nums[0]]]
        res = []
        for i in range(len(nums)):
            for l in self.recursion(nums[:i]+nums[i+1:]):
                res.append([nums[i]] + l)
        return res

if __name__ == '__main__':
    print(Solution().permute([1]))

# 题解
# 使用递归，每次选择一个数字 X，然后将除 X 之外的数字递归进行全排列，最后将 X 放在每个结果的最前面，就是全排列。