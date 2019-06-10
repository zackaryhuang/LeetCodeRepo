class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=nums1+nums2
        nums.sort()
        length=len(nums)
        if length%2==1:
            return float(nums[int(length/2)])
        else:
            mid=int(length/2)
            #print(nums[mid])
            #print(nums[mid+1])
            return float((nums[mid-1]+nums[mid])/2)
        
