class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]
        nums.sort(reverse = True)
        candidates = []
        while len(nums) > 0 and len(candidates) < 6:
            candidates.append(nums[0])
            nums.pop(0)
            if len(nums) > 0:
                candidates.append(nums[-1])
                nums.pop(-1)
        bigger_than_zero = []
        less_than_zero = []
        equal_to_zero = []
        for i in candidates:
            if i > 0:
                bigger_than_zero.append(i)
            elif i < 0:
                less_than_zero.append(i)
            else:
                equal_to_zero.append(i)
        result = []
        bigger_than_zero.sort(reverse = True)
        less_than_zero.sort()
        result = []
        # 3 +
        if len(bigger_than_zero) > 2:
            result.append(bigger_than_zero[0] * bigger_than_zero[1] * bigger_than_zero[2])
        # 2 + 1 -
        if len(bigger_than_zero) > 1 and len(less_than_zero) > 0:
            result.append(bigger_than_zero[0] * bigger_than_zero[1] * less_than_zero[-1])
        # 2 - 1 +
        if len(less_than_zero) > 1 and len(bigger_than_zero) > 0:
            result.append(less_than_zero[0] * less_than_zero[1] * bigger_than_zero[0])
        if len(less_than_zero) > 2:
            result.append(less_than_zero[0] * less_than_zero[1] * less_than_zero[2])
        result.append(0)
        return max(result)




        # num1 = nums[0]
        # if num1 < abs(nums[len(nums) - 1]):
        #     num1 = nums[len(nums) - 1]
        #     nums.pop(len(nums) - 1)
        # else:
        #     nums.pop(0)
        #
        # num2 = nums[0]
        # if num2 < abs(nums[len(nums) - 1]):
        #     num2 = nums[len(nums) - 1]
        #     nums.pop(len(nums) - 1)
        # else:
        #     nums.pop(0)
        # print(num1,num2)
        # print(nums)
        # if num1 * num2 > 0:
        #     return num1 * num2 * max(nums)
        # else:
        #     return num1 * num2 * min(nums)

if __name__ == '__main__':
    s = Solution()
    print(s.maximumProduct([1,2,-34,-2]))
