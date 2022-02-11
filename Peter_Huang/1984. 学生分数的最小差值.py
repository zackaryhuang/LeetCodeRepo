class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        a = [2,3,4,5,6]
        print(a[:3])
        nums.sort()
        min_res = 0
        if len(nums) < k:
            return min_res
        min_res = max(nums[:k]) - min(nums[:k])
        for i in range(len(nums) - k + 1):
            temp = nums[i + k - 1] - nums[i]
            if temp < min_res:
                min_res = temp
        return min_res


if __name__ == '__main__':
    print(Solution().minimumDifference([87063,61094,44530,21297,95857,93551,9918],6))