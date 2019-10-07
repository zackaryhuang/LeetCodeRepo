class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        newStr = s[::-1]
        index = 0
        meetChar = False
        res = 0
        for char in newStr:
            if char != ' ':
                meetChar = True
                res += 1
            if meetChar and char == ' ':
                return res
        return res



if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLastWord('abc'))

