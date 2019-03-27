import math
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = -x
            string = ''
            string = str(x)
            string = string[::-1]
            print(string)
            res = -int(string)
        else:
            string = ''
            string = str(x)
            string = string[::-1]
            print(string)
            res = int(string)
        if res > math.pow(2,31) - 1 or res < -math.pow(2,31):
            return 0
        else:
            return res