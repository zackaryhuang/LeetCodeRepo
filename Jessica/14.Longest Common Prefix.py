class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        count=0
        length=len(strs)
        if  length==0:
            return ''
        if  length==1:
            return strs[0]
        len0=len(strs[0])
        for i in range(0,len0):
            for j in range(1,length):
                if i==len(strs[j]):
                    return strs[0][0:count]
                if strs[j][i] != strs[j-1][i]:
                    return strs[0][0:count]
                elif j==length-1:
                    count+=1
                else:                
                    continue            
        return strs[0][0:count]