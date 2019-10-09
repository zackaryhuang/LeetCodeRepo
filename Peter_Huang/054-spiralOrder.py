class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        while len(matrix) != 0:
            res.extend(matrix[0])
            matrix.pop(0)
            if len(matrix) == 0:
                return res
            a = []
            for i in range(len(matrix)):
                res.append(matrix[i].pop())
                if matrix[i] == []:
                    a.append(i)
            print(matrix)
            print(a)
            for i in a:
                matrix.remove([])
            if len(matrix) == 0:
                return res
            temp1 = matrix[-1]
            res.extend(temp1[::-1])
            matrix.pop()
            if len(matrix) == 0:
                return res
            temp2 = []
            b = []
            for i in range(len(matrix)):
                temp2.append(matrix[i].pop(0))
                if matrix[i] == []:
                    b.append(i)
            res.extend(temp2[::-1])
            for i in b:
                matrix.remove([])
            if len(matrix) == 0:
                return res
        return res


if __name__ == '__main__':
    s = Solution()
    res = s.spiralOrder([[7],[9],[6]])
    print(res)