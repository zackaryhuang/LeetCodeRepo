"""
执行用时 : 32 ms, 在Implement strStr()的Python提交中击败了33.55% 的用户
内存消耗 : 11.8 MB, 在Implement strStr()的Python提交中击败了0.55% 的用户
"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle in haystack:
            index = haystack.index(needle)
            return index
        else:
            return -1
