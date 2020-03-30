class Solution(object):
    def lastRemaining(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        nums = []
        for i in range(n):
            nums.append(i)
        startIndex = (m - 1) % len(nums)
       
        while(len(nums) > 1):
            a = nums.pop((startIndex) % len(nums))
            print(a)
            startIndex = (startIndex + m - 1) % len(nums)
        return nums[0]
if __name__ == "__main__":
    s = Solution()
    print(s.lastRemaining(10,17))