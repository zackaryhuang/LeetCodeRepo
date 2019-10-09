class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while len(nums) != 0:
            temp = nums.pop()
            if temp in nums:
                nums.remove(temp)
            else:
                return temp
if __name__ == '__main__':
    s = Solution()
    res = s.singleNumber([1,22,3,3,22,1,7])
    print(res)