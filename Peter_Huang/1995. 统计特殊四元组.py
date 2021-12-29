class Solution(object):
    def countQuadruplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for a in range(len(nums)-3):
            for b in range(a+1, len(nums)-2):
                for c in  range(b+1, len(nums)-1):
                    for d in range(c+1, len(nums)):
                        if nums[a] + nums[b] + nums[c] == nums[d]:
                            res += 1
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.countQuadruplets([1,1,1,3,5]))
