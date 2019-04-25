class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return '1'
        if n==2:
            return '11'
        currentStr='11'        
        for i in range (3,n+1):            
            count=1
            ret=''
            for j in range(1,len(currentStr)):
                if currentStr[j]==currentStr[j-1]:
                    count+=1
                else:                    
                    ret+=str(count)+currentStr[j-1]
                    count=1                    
                if j==len(currentStr)-1:
                    ret+=str(count)+currentStr[j]
            currentStr=ret
        return ret
                    
            
            
            
            
        
