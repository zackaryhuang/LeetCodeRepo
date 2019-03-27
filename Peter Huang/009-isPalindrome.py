class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        int_to_str = str(x)
        str_length = len(int_to_str)
        for i in range(0,int(str_length/2)):
            if int_to_str[i] == int_to_str[str_length - 1]:
                str_length -= 1
                continue
            else:
                return False
        return True
                