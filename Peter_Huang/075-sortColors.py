class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        lastZeroIndex = 0
        lastOneIndex = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if i == 0:
                    continue
                else:
                    for j in range(lastZeroIndex + 1, i):
                        nums[j + 1] = nums[j]
                    nums[lastZeroIndex + 1] = 0
                    lastZeroIndex += 1
                print(nums)
            elif nums[i] == 1:
                if i == 0:
                    continue
                else:
                    for j in range(lastOneIndex + 1, i):
                        nums[j + 1] = nums[j]
                    nums[lastOneIndex + 1] = 1
                    lastOneIndex += 1
                print(nums)
            else:
                continue
                print(nums)
        return nums

if __name__ == "__main__":
    s = Solution()
    res = s.sortColors([2,1,2,1,0,0,2])
    print(res)