from tracemalloc import start


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        candidates = []
        for i in range(len(nums[::-1])):
            num = nums[::-1][i]
            if len(candidates) == 0 or num >= max(candidates):
                candidates.append(num)
                continue
            else:
                min_index = len(candidates) - 1
                min_candidate = candidates[min_index]
                for index in range(len(candidates)):
                    if candidates[index] > num and candidates[index] < min_candidate:
                        min_candidate = candidates[index]
                        min_index = index
                nums[len(nums) - i - 1] = min_candidate
                nums[len(nums) - min_index - 1] = num
                self.bubleSort(nums, len(nums) - i)
                return
        nums.sort()

    def bubleSort(self, nums, startIndex):
        n = len(nums)
        for i in range(startIndex, n):
            for j in range(startIndex, n-1):
                if nums[j] > nums[j+1] :
                    nums[j], nums[j+1] = nums[j+1], nums[j]

if __name__ == '__main__':
    nums = [5,4,7,5,3,2]
    print(Solution().nextPermutation(nums))

# 题解
# 倒序遍历数组，找到第一个比后面的数大的数 X，然后和后面的最小的且大于 X 的数交换位置，然后把 X 后面的数按照升序排列

