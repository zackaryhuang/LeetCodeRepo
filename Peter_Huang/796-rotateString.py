class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A == B:
            return True
        for i in range(len(A)):
            if A[i:] + A[:i] == B:
                return True
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.rotateString("abcde","abced"))