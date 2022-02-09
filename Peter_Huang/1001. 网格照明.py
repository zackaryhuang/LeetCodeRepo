from re import M

from pip import main


class Solution(object):
    def gridIllumination(self, n, lamps, queries):
        """
        :type n: int
        :type lamps: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        for query in queries:
            query_x = query[0]
            query_y = query[1]
            lighted = False
            for lamp in lamps:
                lamp_x = lamp[0]
                lamp_y = lamp[1]
                if lamp_x < 0 or lamp_y < 0:
                    continue
                if query_x == lamp_x or query_y == lamp_y or (query_x - lamp_x) == (query_y - lamp_y) or (query_x - lamp_x) == (lamp_y - query_y):
                    lighted = True
            if lighted:
                ans.append(1)
            else:
                ans.append(0)
            for lamp in lamps:
                lamp_x = lamp[0]
                lamp_y = lamp[1]
                if lamp_x <= query_x + 1 and lamp_x >= query_x - 1 and lamp_y <= query_y + 1 and lamp_y >= query_y - 1:
                    lamp[0] = -1
                    lamp[1] = -1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.gridIllumination(5, [[0,0],[1,0]], [[1,1],[1,1]]))
            