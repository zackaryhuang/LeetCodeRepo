from urllib3 import Retry


class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                num_front = nums[i]
                num_back = nums[j]
                if num_front - num_back == k or num_front - num_back == -k:
                    ans += 1
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.countKDifference([1,2,2,1], 1))

