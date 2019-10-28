import copy
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return  [1,1]
        if rowIndex == 2:
            return [1,2,1]
        if rowIndex == 3:
            return [1,3,3,1]
        a = (rowIndex // 2) - 1
        res = [1,rowIndex]
        for i in range(0,a):
            res.append(res[-1] * (rowIndex - i - 1)/(2 + i))
        temp = copy.copy(res)
        if rowIndex % 2 == 0:
            temp.pop()
        for i in temp[::-1]:
            res.append(i)
        return res

if __name__ == '__main__':
    s = Solution()
    res = s.getRow(7)
    print(res)