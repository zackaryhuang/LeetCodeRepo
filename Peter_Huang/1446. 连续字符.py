class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_char = ''
        max_length = 0
        cur_length = 0
        for char in s:
            if char == last_char:
                cur_length += 1
            else:
                cur_length = 1
                last_char = char
            max_length = max(cur_length, max_length)
        return max_length


if __name__ == '__main__':
    s = Solution()
    print(s.maxPower("leetcode"))
