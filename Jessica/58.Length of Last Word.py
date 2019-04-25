class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count=0
        for i in range(len(s),0,-1):            
            if s[i-1]!=' ':
                count+=1
            else:
                if count==0:
                    continue
                else:
                    return count
        return count
        
