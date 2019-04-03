"""
执行用时 : 84 ms, 在Roman to Integer的Python提交中击败了99.48% 的用户
内存消耗 : 11.8 MB, 在Roman to Integer的Python提交中击败了0.47% 的用户

用到了hash dict
"""
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=0
        i=0
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        while(i<len(s)-1):
            if(d[s[i]]>=d[s[i+1]]):
                a=a+d[s[i]];
                i=i+1
            else:
                a=a+d[s[i+1]]-d[s[i]]
                i=i+2
        l=len(s)
        if(d[s[l-2]]>=d[s[l-1]]):
            a=a+d[s[l-1]]
        return a
       """"
       改进版代码
       a=0
       d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
       for i in range(len(s)):
            if(i<len(s)-1 and d[s[i]]<d[s[i+1]]):
                a-=d[s[i]]
            else:
                a+=d[s[i]]
       """"
        
