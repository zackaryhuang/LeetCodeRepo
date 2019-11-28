class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        sumOfRow = len(matrix)
        sumOfCol = len(matrix[0])
        for i in range(sumOfRow - 1):
            for j in range(sumOfCol - 1):
                print('a:', matrix[i][j])
                print('b:', matrix[i+1][j+1])
                if matrix[i][j] == matrix[i+1][j+1]:
                    continue
                else:
                    return False
        return True
            


if __name__ == "__main__":
    s = Solution()
    res = s.isToeplitzMatrix([[1,2],[2,2]])
    print(res)