"""
执行用时 : 32 ms, 在Letter Combinations of a Phone Number的Python提交中击败了17.05% 的用户
内存消耗 : 11.9 MB, 在Letter Combinations of a Phone Number的Python提交中击败了0.93% 的用户
dict
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        KEY = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']}
        if(digits==''):
            return []
        ans = ['']
        for i in digits:
            ans = [pre+suf for pre in ans for suf in KEY[i]]
        return ans
