"""
执行用时 : 244 ms, 在Container With Most Water的Python提交中击败了2.53% 的用户
内存消耗 : 13.2 MB, 在Container With Most Water的Python提交中击败了0.85% 的用户
双指针法
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max=0
        left=0
        right=len(height)-1
        while(left<right):
            l=right-left
            if(height[left]<height[right]):
                h=height[left]
                left+=1
            else:
                h=height[right]
                right-=1
            area=l*h
            if(max<area):
                max=area
        return max
