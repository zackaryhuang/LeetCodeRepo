from typing import List

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = list(zip(difficulty, profit))
        jobs.sort()
        ret = best = i = 0
        for skill in sorted(worker):
            while(i < len(jobs) and skill >= jobs[i][0]):
                best = max(best, jobs[i][1])
                i += 1
            ret += best
        return ret

s = Solution()
print(s.maxProfitAssignment([4,2,6,8,10], [20,10,30,40,50], [4,5,6,7]))