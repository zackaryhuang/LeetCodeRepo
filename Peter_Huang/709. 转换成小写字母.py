class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        for index in range(len(s)):
            ascii_char = ord(s[index])
            if 65 <= ascii_char <= 90:
                char = chr(ascii_char + 32)
                s = s[:index] + char + s[index+1:]
        return s


if __name__ == '__main__':
    s = Solution()
    print(s.toLowerCase('ZEBRA'))
