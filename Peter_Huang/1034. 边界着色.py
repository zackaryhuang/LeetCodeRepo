class Solution(object):
    def colorBorder(self, grid, row, col, color):
        """
        :type grid: List[List[int]]
        :type row: int
        :type col: int
        :type color: int
        :rtype: List[List[int]]
        """
        candidate_for_fill = []
        self.dfs(grid, row, col, grid[row][col], candidate_for_fill)
        wait_for_fill = []
        for pos in candidate_for_fill:
            if self.isValidBorder(grid, pos[0], pos[1], grid[row][col]):
                wait_for_fill.append(pos)
        for pos in wait_for_fill:
            grid[pos[0]][pos[1]] = color
        return grid

    def isValidBorder(self, grid, row, col, target_color):
        grid_w = len(grid[0])
        grid_h = len(grid)
        if row == 0 or row == grid_h - 1 or col == 0 or col == grid_w - 1:
            return True
        if row - 1 >= 0 and grid[row - 1][col] != target_color:
            return True
        if row + 1 < grid_h and grid[row + 1][col] != target_color:
            return True
        if col - 1 >= 0 and grid[row][col - 1] != target_color:
            return True
        if col + 1 < grid_w and grid[row][col + 1] != target_color:
            return True
        return False

    def dfs(self, grid, row, col, target_color, candidate_for_fill):
        grid_w = len(grid[0])
        grid_h = len(grid)
        if 0 <= row < grid_h and 0 <= col < grid_w:
            if grid[row][col] == target_color and (row, col) not in candidate_for_fill:
                candidate_for_fill.append((row, col))
                self.dfs(grid, row - 1, col, target_color, candidate_for_fill)
                self.dfs(grid, row + 1, col, target_color, candidate_for_fill)
                self.dfs(grid, row, col - 1, target_color, candidate_for_fill)
                self.dfs(grid, row, col + 1, target_color, candidate_for_fill)
        return


if __name__ == '__main__':
    s = Solution()
    print(s.colorBorder([[1,1],[1,2]], 0, 0, 3))
