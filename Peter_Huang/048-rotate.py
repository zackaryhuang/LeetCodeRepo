class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for i in range(0, len(matrix)):
            for j in range(i, len(matrix)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        print(matrix)
        for j in range(0, len(matrix)):
            c = len(matrix[j]) // 2
            for i in range(0, c):
                temp = matrix[j][i]
                matrix[j][i] = matrix[j][-i-1]
                matrix[j][-i-1] = temp
        print(matrix)

if __name__ == "__main__":
    s = Solution()
    res = s.rotate([[1,2,3],[4,5,6],[7,8,9]])