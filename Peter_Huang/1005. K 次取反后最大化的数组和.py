class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)):
            num = sorted_nums[i]
            if k == 0 or num == 0:
                return sum(sorted_nums)
            if num < 0:
                sorted_nums[i] = -num
                k -= 1
                continue
            else:
                break
        sorted_nums = sorted(sorted_nums)
        sorted_nums[0] = sorted_nums[0] * (-1) ** k
        return sum(sorted_nums)


if __name__ == '__main__':
    s = Solution()
    print(s.largestSumAfterKNegations([4,2,3], 1))
