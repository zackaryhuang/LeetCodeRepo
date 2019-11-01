class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if len(s) < k:
            return s
        elif len(s) >= k and len(s) < 2 * k:
            return (s[:k])[::-1] + s[k:]
        else:
            return (s[:k])[::-1] + s[k:2 * k] + self.reverseStr(s[2 * k:], k)

if __name__ == "__main__":
    s = Solution()
    res = s.reverseStr('abcdefg',2)
    print(res)
            