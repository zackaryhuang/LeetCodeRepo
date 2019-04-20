class Solution:
    def romanToInt(self, s: str) -> int:
        dict1={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ret=dict1[s[0]]
        if len(s)==1:
            return ret
        for i in range(1,len(s)):
            if s[i]=='V' and s[i-1]=='I':
                ret=ret+3
            elif s[i]=='X' and s[i-1]=='I':
                ret=ret+8
            elif s[i]=='L' and s[i-1]=='X':
                ret=ret+30
            elif s[i]=='C' and s[i-1]=='X':
                ret=ret+80
            elif s[i]=='D' and s[i-1]=='C':
                ret=ret+300
            elif s[i]=='M' and s[i-1]=='C':
                ret=ret+800
            else:
                ret=ret+dict1[s[i]]
        return ret