"""
执行用时 : 36 ms, 在Generate Parentheses的Python提交中击败了33.55% 的用户
内存消耗 : 12.2 MB, 在Generate Parentheses的Python提交中击败了0.00% 的用户
"""
def dfs(left,right,str,ans):
    if(left>right):
        return
    elif(left==0 and right==0):
        ans.append(str)
    else:
        if(left>0):
            dfs(left-1,right,str+'(',ans)
        if(right>0):
            dfs(left,right-1,str+')',ans)
class Solution(object):
    
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        s=''
        ans=[]
        dfs(n,n,s,ans)
        return ans
