class Solution(object):
    def plusOne(self, digits):
        newDigits = digits[::-1]
        num = 0
        for i in range(len(newDigits)):
            num += newDigits[i] * (10 ** i)
        num += 1
        numStr = str(num)
        res = []
        for char in numStr:
            res.append(int(char))
        return res


if __name__ == '__main__':
    s = Solution()
    s.plusOne([1,2,3])

