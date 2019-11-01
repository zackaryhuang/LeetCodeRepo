class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        if n == 1:
            return True
        b = n % 2
        n = n / 2
        if n == 1 and b == 0:
            return True
        elif b == 0:
            return self.isPowerOfTwo(n)
        else:
            return False


if __name__ == "__main__":
    s = Solution()
    res = s.isPowerOfTwo(0)
    print(res)