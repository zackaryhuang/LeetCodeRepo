from turtle import st


class Solution(object):
    def simplifiedFractions(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                c = self.simplify(i, j)
                if c not in res:
                    res.append(self.simplify(i, j))
        return res
    
    def simplify(self, numerator, denominator):
        if numerator == 1:
            return '1/' + str(denominator)
        for i in range(2, denominator):
            if numerator % i == 0 and denominator % i == 0:
                return self.simplify(numerator // i, denominator // i)
        return str(numerator) + '/' + str(denominator)

if __name__ == '__main__':
    print(Solution().simplifiedFractions(7))