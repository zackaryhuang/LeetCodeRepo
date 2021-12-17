class Solution(object):
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        richer_count = len(quiet)
        group = [[] for _ in range(richer_count)]
        for rich in richer:
            group[rich[1]].append(rich[0])

        ans = [-1] * richer_count

        def dfs(x):
            if ans[x] != -1:
                return
            ans[x] = x
            for y in group[x]:
                dfs(y)
                if quiet[ans[y]] < quiet[ans[x]]:
                    ans[x] = ans[y]
        for i in range(richer_count):
            dfs(i)
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.loudAndRich([[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], [3,2,5,4,6,1,7,0]))
