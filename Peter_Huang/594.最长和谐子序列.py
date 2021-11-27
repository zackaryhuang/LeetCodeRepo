from collections import Counter


class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        print(nums)
        max_length = 0
        for i in range(len(nums)):
            l = []
            for j in range(i, len(nums)):
                if len(l) < 2:
                    l.append(nums[j])
                    if j == len(nums) - 1 and max(l) - min(l) == 1:
                        max_length = max(max_length, len(l))
                elif max(l) - min(l) <= 1:
                    if max(l) - min(l) == 1:
                        max_length = max(max_length, len(l))
                    l.append(nums[j])
                    if j == len(nums) - 1 and max(l) - min(l) == 1:
                        max_length = max(max_length, len(l))
                else:
                    break
        return max_length



s = Solution()
Counter([1,2,3]).values()
print(s.findLHS([1,2,2,1]))