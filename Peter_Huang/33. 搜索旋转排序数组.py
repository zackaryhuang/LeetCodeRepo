class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i, num in enumerate(nums):
            if num == target:
                return i
        return -1


if __name__ == '__main__':
    nums = [5, 4, 7, 5, 3, 2]
    print(Solution().search(nums, 5))