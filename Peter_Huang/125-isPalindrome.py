
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 将所有字符转化为小写
        s = s.lower()
        print(s)
        news = ''
        for char in s:
            if char in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']:
                news += char
        print(news)
        return news == news[::-1]


if __name__ == '__main__':
    s = Solution()
    res = s.isPalindrome('0P')
    print(res)

