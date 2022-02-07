from pip import main


class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        res = ""
        while a > 0 or b > 0 or c > 0:
            if a >= b and a >= c and self.canAppend(res, 'a'):
                res += 'a'
                a -= 1
            elif b >= a and b >= c and self.canAppend(res, 'b'):
                res += 'b'
                b -= 1
            elif c >= a and c >= b and self.canAppend(res, 'c'):
                res += 'c'
                c -= 1
            else:
                if a > 0 and self.canAppend(res, 'a'):
                    res += 'a'
                    a -= 1
                elif b > 0 and self.canAppend(res, 'b'):
                    res += 'b'
                    b -= 1
                elif c > 0 and self.canAppend(res, 'c'):
                    res += 'c'
                    c -= 1
                else:
                    break
        return res
    
    def canAppend(self, res, target):
        if len(res) < 2:
            return True
        if res[-1] == res[-2] == target:
            return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.longestDiverseString(7,1,0))
    print(s.longestDiverseString(1,1,7))
    print(s.longestDiverseString(2,2,1))