class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        sorted_array = []
        nums1_length = len(nums1)
        nums2_length = len(nums2)
        while len(nums1) != 0 and len(nums2) != 0:
            if nums1[i] <= nums2[i]:
                sorted_array.append(nums1[i])
                nums1.pop(0)
            else:
                sorted_array.append(nums2[i])
                nums2.pop(0)
        if len(nums1) == 0:
            for num in nums2:
                sorted_array.append(num)
        if len(nums2) == 0:
            for num in nums1:
                sorted_array.append(num)
        temp = int(len(sorted_array) / 2)
        if len(sorted_array) % 2 ==0:
            median = (sorted_array[temp-1] + sorted_array[temp]) / 2
            return median
        else:
            median = sorted_array[temp]
            return median
