class Solution:
    def reverse(self, x: int) -> int:
        if x>2147483647 or x< -2147483648:
            return 0
        flag=0
        ret=0
        if x<0:
            flag=1
            x=abs(x)
        str1=str(x)
        
        if flag==1:
            ret=-1*int(str1[::-1])
        else:
            ret=int(str1[::-1])
        
        if ret>2147483647 or ret< -2147483648:
            return 0
        else:
            return ret