class Solution(object):
    def repeatedStringMatch(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        res = 1
        temp = a
        c = 0
        while (len(a) < len(b) or b not in a) and c <= 2:
            a += temp
            res += 1
            if len(a) > len(b):
                c += 1
        if b in a:
            return res
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.repeatedStringMatch("abc", "cabcabca"))
