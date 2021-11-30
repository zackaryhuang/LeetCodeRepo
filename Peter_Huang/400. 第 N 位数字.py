class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 9:
            return n
        dig_count = n // 9
        dig_len = len(str(dig_count))
        flag = len(str(dig_count))
        sum = 0
        for i in range(1, dig_len+1):
            sum += i * 10 ** (i-1)
        if n <= sum * 9:
            sum = 0
            for i in range(1, dig_len):
                sum += i * 10 ** (i - 1)
        else:
            flag += 1
        a = (n - sum * 9) // flag
        if a == 0:
            a += 1
        b = (n - sum * 9) % flag
        a += int('9'*len(str(sum)))
        return int(str(a)[-1]) if b == 0 else int(str(a+1)[b-1])


if __name__ == '__main__':
    s = Solution()
    print(s.findNthDigit(100))