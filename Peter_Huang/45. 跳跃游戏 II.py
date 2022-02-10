import enum
from operator import index


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            maxPos = max(maxPos, i + nums[i])
            if i == end:
                end = maxPos
                step += 1
        return step

if __name__ == '__main__':
    print(Solution().jump([2, 3, 1]))

