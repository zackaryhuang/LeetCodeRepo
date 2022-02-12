class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while num > 0:
            num -= i
            i += 2
        if num == 0:
            return True
        return False

s = Solution()
print(s.isPerfectSquare(25))