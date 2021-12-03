class Solution(object):
    def leastMinutes(self, n):
        """
        :type n: int
        :rtype: int
        """
        min_square = 0
        while(2 ** (min_square + 1) <= n):
            min_square += 1
        x = (n - 2 ** min_square) // (2 ** min_square)
        y = (n - 2 ** min_square) % (2 ** min_square)
        # print(x, y, min_square)
        return min_square + 1 if (x == 0 and y == 0) else (min_square + x + 1 + (o if y == 0 else 1))