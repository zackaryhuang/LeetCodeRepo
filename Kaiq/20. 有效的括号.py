"""
执行用时 : 84 ms, 在Valid Parentheses的Python提交中击败了2.41% 的用户
内存消耗 : 11.9 MB, 在Valid Parentheses的Python提交中击败了2.24% 的用户
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while('()' in s or '{}' in s or '[]' in s):
            s=s.replace('()','')
            s=s.replace('[]','')
            s=s.replace('{}','')
        return s ==''
