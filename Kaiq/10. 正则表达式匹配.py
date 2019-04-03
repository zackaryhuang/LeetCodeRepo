"""
执行用时 : 88 ms, 在Regular Expression Matching的Python提交中击败了54.69% 的用户
内存消耗 : 11.9 MB, 在Regular Expression Matching的Python提交中击败了0.00% 的用户

导入了re正则包
group(0) 将所有匹配符合条件的字符串，打包成一个组，即group。
        其中编号为0的group，即group(0)表示匹配的整个字符串

"""
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        import re
        ans = re.match(p,s)
        print ans
        if(ans ==None):
            return 0
        print ans.group(0)
        if(ans.group(0)!=s):
            return 0
        return 1
