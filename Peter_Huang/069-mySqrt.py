class Solution(object):
    def mySqrt(self, x):
        a = 0
        while (a ** 2) <= x:
            a += 1
        return a - 1

if __name__ == '__main__':
    s = Solution()
    res = s.mySqrt(100)
    print(res)
