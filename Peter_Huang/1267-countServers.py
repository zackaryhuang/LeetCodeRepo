class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        m = len(grid)
        n = len(grid[0])
        # print(m,n)
        for i in range(m):
            for j in range(n):
                print(i,j)
                if grid[i][j] == 1 and self.canLinkToAnotherServer(i, j, grid):
                    # print(i,j)
                    count += 1
        return count

    def canLinkToAnotherServer(self, x, y, grid):
        m = len(grid)
        n = len(grid[0])
        for i in range(0,m):
            if i == x:
                continue
            else:
                if grid[i][y] == 1:
                    return True
        for i in range(0, n):
            if i == y:
                continue
            else:
                if grid[x][i] == 1:
                    return True
        return False

if __name__ == "__main__":
    s = Solution()
    print(s.countServers([
    [1,0,0,1,0],
    [0,0,0,0,0],
    [0,0,0,1,0]]))
