class Solution(object):
    def divide(self, dividend, divisor):
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        res = 0
        if divisor == 1:
            res = dividend
        if divisor == -1:
            res = -dividend
        if divisor == dividend:
            res = 1
        if dividend == 0:
            return 0
        if divisor == -dividend:
            res = -1
        if ((res < INT_MIN) or (res > INT_MAX)):
            return INT_MAX
        sign = 1
        # 1.判断符号
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            sign = -1
        
        if sign == 1:
            m = divisor
            n = 1
            if dividend > 0:
                if dividend < divisor:
                    return 0
                while(dividend >= (m + m)):
                    m += m
                    n += n
            else:
                if dividend > divisor:
                    return 0
                while(dividend <= (m + m)):
                    m += m
                    n += n
            return n + self.divide(dividend - m, divisor)
        else:
            x = divisor
            y = 1
            if dividend > 0:
                if -dividend > divisor:
                    return 0
                while(dividend >= -(x + x)):
                    x += x
                    y += y
            else:
                if -dividend < divisor:
                    return 0
                while(dividend <= -(x + x)):
                    x += x
                    y += y
            return -y + self.divide(dividend + x, divisor)

s = Solution()
print(s.divide(10123123123123, 3))