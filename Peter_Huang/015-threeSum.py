import copy
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i == 0 or nums[i] > nums[i-1]:
                left = i+1
                right = len(nums)-1
                while left < right:
                    sum = nums[i] + nums[left] + nums[right]
                    if sum == 0:
                        temp = [nums[i],nums[left],nums[right]]
                        res.append(temp)
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                    elif sum > 0:
                        right -= 1
                    else:
                        left += 1
        return res
    
def main():
    solution = Solution()
    res = solution.threeSum([0,0,0])
    print(res)

if __name__ == "__main__":
    main()