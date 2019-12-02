import copy
class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        dict = {'1' : '1',
                '2' : '5',
                '5' : '2',
                '6' : '9',
                '8' : '8',
                '9' : '6',
                '0' : '0'}
        l = []
        for i in range(1, N + 1):
            s1 = str(i)
            s2 = ''
            for c in s1:
                if c in dict:
                    # print(c)
                    s2 += dict[c]
                else:
                    s2 = s1
                    break
            if s1 != s2:
                print(s2)
                if s1 not in l:
                    l.append(s1)
        return len(l)

if __name__ == "__main__":
    s = Solution()
    res = s.rotatedDigits(857)
    print(res)