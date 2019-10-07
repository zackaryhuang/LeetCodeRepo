class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        return self.iteration(candidates, target, res)

    def iteration(self, candidates, target, res):
        for num in candidates:
            if target == num:
                res.append(num)
                res.append(',')
            elif target < 0:
                return []
            else:
                res.append(num)
                self.iteration(candidates, target - num, res)
        return res


if __name__ == "__main__":
    s = Solution()
    res = s.combinationSum([1, 2, 3], 4)
    print(res)
