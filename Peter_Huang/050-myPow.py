class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n > 2 ** 31 -1 or n < 2 ** 31:
            return 0.0
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n == -1:
            return 1 / x
        else:
            half = self.myPow(x, n / 2)
            rest = self.myPow(x, n % 2)
            return half * half *rest

if __name__ == "__main__":
    s = Solution()
    res = s.myPow(0.00001, 2147483647)
    print(res)