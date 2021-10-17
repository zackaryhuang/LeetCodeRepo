from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k < 1 or n < k:
            return []
        ret = []
        path = []
        self.dfs(n, k, 1, ret, path)
        return ret

    def dfs(self, n, k, start, res, path):
        if len(path) == k:
            res.append(path[:])
            return
        for num in range(start, n+1):
            path.append(num)
            self.dfs(n, k, num + 1, res, path)
            path.pop()

s = Solution()
print(s.combine(4, 2))