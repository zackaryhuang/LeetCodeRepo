class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # f(i) = max(f(i-2) + A_i, f(i-1))
        # f(-1) = f(0) = 0
        preMax = 0
        curMax = 0
        for num in nums:
            temp = curMax
            curMax = max(preMax + num, curMax)
            preMax = temp
        return curMax

if __name__ == "__main__":
    s = Solution()
    res = s.rob([1,2,3,1])
    print(res)