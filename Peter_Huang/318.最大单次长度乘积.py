class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words = sorted(words, key=len, reverse=True)
        makes = []
        for word in words:
            m = 0
            for c in word:
                m |= 1 << ord(c) - ord('a')
            makes.append(m)
        max_len = 0
        for i in range(len(makes)):
            m = makes[i]
            for j in range(i+1, len(makes)):
                n = makes[j]
                if m & n == 0:
                    length = len(words[i]) * len(words[j])
                    if length > max_len:
                        max_len = length
        return max_len


s = Solution()
print(s.maxProduct(["a","ab","abc","d","cd","bcd","abcd"]))
# print(bin(1 << 10))