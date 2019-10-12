import itertools as it
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) > 12:
            return []
        index = []
        a = []
        res = []
        for i in range(1,len(s)):
            index.append(i)
        newIndex = it.combinations(index, 3)
        for i in newIndex:
            b = [s[:i[0]], s[i[0]:i[1]], s[i[1]:i[2]], s[i[2]:]]
            a.append(b)
        for i in a:
            if self.isValid(i):
                str = ''
                str += i[0] + '.' + i[1] + '.' + i[2] + '.' + i[3]
                res.append(str)
        return res

    def isValid(self, l):
        # if l[0] == '0':
        #     return l[1] == '0' and l[2] == '0' and l[3] == '0'
        for i in l:
            if len(i) > 1 and i[0] == '0':
                return False
            if 256 > int(i) >= 0:
                continue
            else:
                return False
        return True




if __name__ == '__main__':
    s = Solution()
    res = s.restoreIpAddresses("00000")
    print(res)