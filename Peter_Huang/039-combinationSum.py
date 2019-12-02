import copy
class Solution(object):
    def combinationSum(self, candidates, target):
        size = len(candidates)
        if size == 0:
            return []
        candidates.sort()
        path = []
        res = []
        self.iteration(candidates, target, path, 0, res, size)
        return res

    def iteration(self, candidates, target, path, beigin, res, size):
        if target == 0:
            res.append(copy.copy(path))
        for index in range(beigin, size):
            rest = target - candidates[index]
            if rest < 0:
                break
            else:
                path.append(candidates[index])
                self.iteration(candidates, rest, path, index, res, size)
                path.pop()
        



if __name__ == "__main__":
    s = Solution()
    res = s.combinationSum([1, 2, 3], 4)
    print(res)
