from sqlite3 import Row
from turtle import pos, position


class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_count = len(grid)
        col_count = len(grid[0])
        exit_positions = []
        total_land_count = 0
        for row in range(row_count):
            for col in range(col_count):
                if (row == 0 or row == row_count - 1 or col == 0 or col == col_count - 1) and grid[row][col] == 1:
                    exit_positions.append([row, col])
                if grid[row][col] == 1:
                    total_land_count += 1
        if len(exit_positions) == 0:
            return 0
        temp = []
        for postion in exit_positions:
            for p in self.canExitPositions(postion, grid, []):
                if p not in temp:
                    temp.append(p)
        return total_land_count - len(temp)

    def canExitPositions(self, exit_position, grid, positions):
        positions.append(exit_position)
        row, col = exit_position[0], exit_position[1]
        # 左
        if col - 1 >= 0 and grid[row][col - 1] == 1 and [row, col - 1] not in positions:
            self.canExitPositions([row, col - 1], grid, positions) 
        # 上
        if row - 1 >= 0 and grid[row - 1][col] == 1 and [row - 1, col] not in positions:
            self.canExitPositions([row - 1, col], grid, positions)
        # 右
        if col + 1 < len(grid[0]) and grid[row][col + 1] == 1 and [row, col + 1] not in positions:
            self.canExitPositions([row, col + 1], grid, positions)
        # 下
        if row + 1 < len(grid) and grid[row + 1][col] == 1 and [row + 1, col] not in positions:
            self.canExitPositions([row + 1, col], grid, positions)
        return positions





if __name__ == '__main__':
    print(Solution().numEnclaves([
        [0,0,0,1,1,1,0,1,0,0],
        [1,1,0,0,0,1,0,1,1,1],
        [0,0,0,1,1,1,0,1,0,0],
        [0,1,1,0,0,0,1,0,1,0],
        [0,1,1,1,1,1,0,0,1,0],
        [0,0,1,0,1,1,1,1,0,1],
        [0,1,1,0,0,0,1,1,1,1],
        [0,0,1,0,0,1,0,1,0,1],
        [1,0,1,0,1,1,0,0,0,0],
        [0,0,0,0,1,1,0,0,0,1]]))

# 题解
# 根据边界上的 1 ，反向寻找所有可以走到网格边界的点 Y，然后用网格中所有为 1 的点的数量 X 减去 Y 即为所求