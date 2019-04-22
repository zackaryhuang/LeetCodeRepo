class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        lcp=strs[0]        
        for i in range(0,len(lcp)):
            for i in strs:
                if i.startswith(lcp):
                    continue
                else:
                    lcp=lcp[:-1]
        return lcp
        
