class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        res = [[1],[1,1]]
        for i in range(3, numRows + 1):
            temp = [1]
            for j in range(len(res[-1]) - 1):
                temp.append(res[i - 2][j] + res[i - 2][j+1])
            temp.append(1)
            res.append(temp)
        return res

if __name__ == '__main__':
    s = Solution()
    res = s.generate(5)
    print(res)

