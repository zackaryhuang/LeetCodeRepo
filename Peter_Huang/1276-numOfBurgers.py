import math
class Solution(object):
    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        """
        :type tomatoSlices: int
        :type cheeseSlices: int
        :rtype: List[int]
        """
        # x = 0
        # y = 0
        # while (4 * x + 2 * y <= tomatoSlices) and (x + y <= cheeseSlices) and x >= 0 and y >= 0 :
        #     while (4 * x + 2 * y <= tomatoSlices) and (x + y <= cheeseSlices) and x >= 0 and y >= 0 :
        #         x += 1
        #         if (4 * x + 2 * y == tomatoSlices) and (x + y == cheeseSlices):
        #             return [x,y]
        #     y += 1
        #     if (4 * x + 2 * y == tomatoSlices) and (x + y == cheeseSlices):
        #         return [x,y]
        # return []
        x = int((tomatoSlices - cheeseSlices * 2) / 2)
        y = int((4 * cheeseSlices - tomatoSlices) / 2)
        if (4 * x + 2 * y == tomatoSlices) and (x + y == cheeseSlices):
            return [x,y]
        return []

if __name__ == "__main__":
    s = Solution()
    print(s.numOfBurgers(73990, 29741))