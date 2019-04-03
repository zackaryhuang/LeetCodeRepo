"""
执行用时 : 36 ms, 在Longest Common Prefix的Python提交中击败了19.10% 的用户
内存消耗 : 11.9 MB, 在Longest Common Prefix的Python提交中击败了0.62% 的用户

先找到最小长度b
然后遍历strs
如果b不在str 则b-1 
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if(strs==[]):
            return ""
        a = min(strs,key=len)
        for str in strs:
            while a not in str[0:len(a)]:
                a = a[:len(a)-1]
        return a
