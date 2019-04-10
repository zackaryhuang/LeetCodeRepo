
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        print(nums)
        closestThreeSum = nums[0] + nums[1] + nums[2]
        for i in range(0,len(nums)-2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                temp = nums[i] + nums[left] + nums[right]
                print("temp:",temp)
                if abs(target - temp) < abs(target - closestThreeSum):
                    closestThreeSum = temp
                if temp > target:
                    right -= 1
                elif temp < target:
                    left += 1
                else:
                    print(target)
                    return target
        print('closestThreeSum:',closestThreeSum)
        return closestThreeSum
                
def main():
    solution = Solution()
    res = solution.threeSumClosest([1,2,4,8,16,32,64,128],82)
    print(res)

if __name__ == "__main__":
    main()
