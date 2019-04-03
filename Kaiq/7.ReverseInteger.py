"""
执行用时 : 40 ms, 在Reverse Integer的Python提交中击败了40.75% 的用户
内存消耗 : 12 MB, 在Reverse Integer的Python提交中击败了2.37% 的用户
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if(x<0):
            x = int('-'+ ((str(x))[1:])[::-1])
        else:
            x = int( (str(x))[::-1]   )
        if( -2**31<x<2**31-1):
            return x
        return 0
