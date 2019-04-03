"""
学会用正则

执行用时 : 44 ms, 在String to Integer (atoi)的Python提交中击败了87.27% 的用户
内存消耗 : 11.7 MB, 在String to Integer (atoi)的Python提交中击败了0.83% 的用户
"""
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        import re
        ret = re.findall(r"^[-+]?\d+",str.strip())
        if(ret):
            ret_str= ret[0]
            if( ret_str[0] == '-' or ret_str[0] == '+'):
                ret_str1 = ret_str[1:]
            else:
                ret_str1 = ret_str
            ret_int = int(ret_str1)
            if( ret_str[0] == '-'):
                return -ret_int if ret_int <= 2**31 else -2**31
            else:
                return ret_int if ret_int < 2**31 else 2**31-1
        else:
            return 0
