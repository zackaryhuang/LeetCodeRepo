class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        strx=str(x)
        length=len(strx)
        str1=strx[0:int(length/2)]
        str2=strx[:-int(length/2)-1:-1]
        if str1 == str2:
            return True
        return False
        
     