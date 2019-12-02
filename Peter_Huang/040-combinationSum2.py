import copy
class Solution(object):
    def combinationSum2(self, candidates, target):
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
            if path not in res:
                res.append(copy.copy(path))
        for index in range(beigin, size):
            rest = target - candidates[index]
            if rest < 0:
                break
            else:
                path.append(candidates[index])
                temp = candidates.pop(index)
                size -= 1
                self.iteration(candidates, rest, path, index, res, size)
                candidates.insert(index, temp)
                size += 1
                path.pop()
        



if __name__ == "__main__":
    s = Solution()
    res = s.combinationSum2([10,1,2,7,6,1,5], 8)
    print(res)
