class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        count = 0
        for i in range(len(s)):
            if s[i] == ' ':
                count += 1
                if count == k:
                    return s[:i]
        return s


if __name__ == '__main__':
    s = Solution()
    print(s.truncateSentence("Hello how are you Contestant", 5))
