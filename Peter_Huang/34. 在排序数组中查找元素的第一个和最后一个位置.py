from turtle import right


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = right = -1
        index = self.binarySearch(nums, 0, len(nums)-1, target)
        if index != -1:
            left = right = index
            while left > 0 and nums[left-1] == target:
                left -= 1
            while right < len(nums)-1 and nums[right+1] == target:
                right += 1
        return [left, right]

    def binarySearch (self, arr, l, r, x): 
        if r >= l: 
            mid = int(l + (r - l)/2)
            if arr[mid] == x: 
                return mid 
            elif arr[mid] > x: 
                return self.binarySearch(arr, l, mid-1, x) 
            else: 
                return self.binarySearch(arr, mid+1, r, x) 
        else: 
            return -1

if __name__ == '__main__':
    print(Solution().searchRange([5,7,7,8,8,10], 8))

# 题解
# 根据二分查找先找到 target 的索引，然后再找到 target 的左右边界