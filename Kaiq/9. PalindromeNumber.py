"""
执行用时 : 108 ms, 在Palindrome Number的Python提交中击败了100.00% 的用户
内存消耗 : 11.7 MB, 在Palindrome Number的Python提交中击败了0.25% 的用户
"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        a = str(x)
        s = a[::-1]
        if(a == s):
            return 1
        else:
            return 0
