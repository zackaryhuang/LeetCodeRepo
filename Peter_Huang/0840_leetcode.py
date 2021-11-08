class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        column = len(grid[0]) 
        ans = 0
        for r in range(row - 2):
            for c in range(column - 2):
                if self.isMagic(grid[r][c], grid[r][c+1], grid[r][c+2],grid[r+1][c],grid[r+1][c+1],grid[r+1][c+2],grid[r+2][c],grid[r+2][c+1],grid[r+2][c+2]):
                    ans += 1
        return ans
                    

    def isMagic(self, a, b, c, d, e, f, g, h, i):
        if e != 5:
            return False
        return ((a+b+c == d+e+f == g+h+i == a+d+g == b+e+h == c+f+i == a+e+i == c+e+g == 15) and sorted([a,b,c,d,e,f,g,h,i]) == list(range(1,10)))

s = Solution()
print(s.numMagicSquaresInside([[4,3,8,4],[9,5,1,9],[2,7,6,2]]))