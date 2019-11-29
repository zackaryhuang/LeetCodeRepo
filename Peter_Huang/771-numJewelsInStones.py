class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        res = 0
        for s in S:
            if s in J:
                res += 1
        return res

if __name__ == "__main__":
    s = Solution()
    res = s.numJewelsInStones('Aa', 'AAAaaBBBBB')
    print(res)