class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tmp=[]
        length=0
        for i in range(0,len(s)):
            if s[i] in tmp:
                length=max(length,len(tmp))
                pos=tmp.index(s[i])
                print(pos)
                tmp=tmp[pos+1:i]
            tmp.append(s[i])
        length=max(length,len(tmp))

        return length
        
