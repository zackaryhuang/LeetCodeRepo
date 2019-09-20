import copy
class Solution(object):
    def removeElement(self, nums, val):
        self.recursion(nums,val)
        print(nums)
        nums2 = copy.copy(nums)
        nums2.reverse()
        count = 0
        for num in nums2:
            if num == None:
                count += 1
            else:
                break
        if count == len(nums):
            return 0
        else:
            return len(nums) - count
    def deleteElementWithIndex(self, nums, index):
        for i in range(index, len(nums)-1):
            nums[i] = nums[i+1]
        nums[len(nums)-1] = None
        return nums

    def recursion(self,nums,val):
        for i in range(0, len(nums)):
            if nums[i] == val:
                nums = self.deleteElementWithIndex(nums,i)
                self.recursion(nums, val)
            else:
                continue

if __name__ == '__main__':
    s = Solution()
    res = s.removeElement([0,1,2,2,3,0,4,2],2)
    print(res)