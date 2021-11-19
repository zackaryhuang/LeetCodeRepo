class Solution(object):
    def __init__(self):
        self.ans = 0

    def integerReplacement(self, n):
        res = 0
        x, y = self.is2square(n)
        if x:
            res += y
            return res

        else:
            if n % 2 == 0:
                res += 1
                return res + self.integerReplacement(n / 2)
            else:
                res += 1
                return res + min(self.integerReplacement(n - 1), self.integerReplacement(n + 1))



    def is2square(self, n):
        s = n
        m = 0
        while(s > 1):
            s = int(s / 2)
            m += 1
        left = n - (2 ** m)
        return (True if left == 0 else False, m)

if __name__ == '__main__':
    s = Solution()
    print(s.integerReplacement(4))
