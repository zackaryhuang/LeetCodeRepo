"""
执行用时 : 800 ms, 在Longest Palindromic Substring的Python提交中击败了56.69% 的用户
内存消耗 : 12 MB, 在Longest Palindromic Substring的Python提交中击败了15.03% 的用户
"""
def ExpandfromCenter(s,left,right):
    l=left
    r=right
    while( l>=0 and r<len(s) and s[l]==s[r] ):
        l=l-1
        r=r+1
    return r-l-1


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if(s.strip()=='' or len(s)==1):
            return s
        start,end = 0,0
        for i in range(0,len(s)):
            len1 = ExpandfromCenter(s,i,i)
            len2 = ExpandfromCenter(s,i,i+1)
            lens = max(len1,len2)
            if(lens> (end-start)):
                start = i-(lens-1)/2
                end = i+ lens/2
        return s[int(start):int(end+1)]










"""
最大划窗法...
暴力法... 可是时间超了
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if(s.strip()==''):
            return s
        if(len(s)==1):
            return s
        
        l=len(s)
        k=l
        c=0
        while(l>0):
            i=0;
            while(l<k-i):
                a=s[i:l+i+1]
                i=i+1
                if(a[::-1] == a):
                    return a
            l=l-1
        return s[0]
        
        
        
        
      
