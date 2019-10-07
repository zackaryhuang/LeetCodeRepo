class Solution(object):
    def addBinary(self, a, b):
        newA = int(a, base=2)
        newB = int(b, base=2)
        c = newA + newB
        res = ''
        while (c // 2) != 0:
            print('商',c // 2)
            print('余',c % 2)
            res += str(c % 2)
            c = c // 2
        res += str(c % 2)
        res = res[::-1]
        print(res)




if __name__ == '__main__':
    s = Solution()
    res = s.addBinary('1001','0001')




