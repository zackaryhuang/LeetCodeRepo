"""
执行用时 : 116 ms, 在Longest Substring Without Repeating Characters的Python提交中击败了23.74% 的用户
内存消耗 : 11.9 MB, 在Longest Substring Without Repeating Characters的Python提交中击败了1.11% 的用户
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr=[]
        temp=0
        max=0
        i=0
        for c in s:
            i=i+1 
            if c not in arr:
                arr.append(c)
                if(len(s)==i):
                    if(max<len(arr)):
                        max=len(arr)
                    
            else:
                temp = len(arr)
                if(max<temp):
                    max=temp
                a = arr.index(c)
                arr.append(c)
                for j in range(0,a+1):
                    del arr[0]
        return max
