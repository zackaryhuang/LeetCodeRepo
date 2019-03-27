"""
执行用时 : 268 ms, 在Median of Two Sorted Arrays的Python提交中击败了2.55% 的用户
内存消耗 : 12.1 MB, 在Median of Two Sorted Arrays的Python提交中击败了3.82% 的用户
"""
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        nums1 = nums1+nums2
        nums1.sort()
        a=len(nums1)
        if(a%2!=0):
            id = (a-1)/2
            return nums1[id]
        else:
            id = a/2
            return float((float(nums1[id])+float(nums1[id-1]))/2)
