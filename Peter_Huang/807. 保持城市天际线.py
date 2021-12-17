class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_rows = []
        max_cols = []
        row_count = len(grid)
        col_count = len(grid[0])
        for r in range(row_count):
            max_rows.append(max(grid[r]))
        for c in range(col_count):
            cols = []
            for r in range(row_count):
                cols.append(grid[r][c])
            max_cols.append(max(cols))
        res = 0
        for r in range(row_count):
            for c in range(col_count):
                c_height = grid[r][c]
                min_height = min(max_cols[c], max_rows[r])
                if c_height < min_height:
                    res += (min_height - c_height)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.maxIncreaseKeepingSkyline([[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]))
