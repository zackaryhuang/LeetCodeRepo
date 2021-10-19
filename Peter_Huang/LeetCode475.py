from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        res = []
        for house in houses:
            m = abs(heaters[-1] - house)
            for heater in heaters:
                m = min(m, abs(heater - house))
            res.append(m)
        return max(res)

        return ret

solution = Solution()

print(solution.findRadius([1,2,3], [2]))