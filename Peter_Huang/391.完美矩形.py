from typing import DefaultDict


class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        min_x = rectangles[0][0]
        min_y = rectangles[0][1]
        max_x = rectangles[0][2]
        max_y = rectangles[0][3]
        total_area = 0
        points = DefaultDict(int)
        for rect in rectangles:
            x_1 = rect[0]
            y_1 = rect[1]
            x_2 = rect[2]
            y_2 = rect[3]

            if x_1 < min_x:
                min_x = x_1
            if x_2 > max_x:
                max_x = x_2
            if y_1 < min_y:
                min_y = y_1
            if y_2 > max_y:
                max_y = y_2
            total_area += (x_2 - x_1) * (y_2 - y_1)
            points[(x_1, y_1)] += 1
            points[(x_2, y_2)] += 1
            points[(x_1, y_2)] += 1
            points[(x_2, y_1)] += 1
        if total_area != ((max_x - min_x) * (max_y - min_y)):
            return False
        if points[(min_x, min_y)] != 1 or points[(max_x, max_y)] != 1 or points[(min_x, max_y)] != 1 or points[(max_x, min_y)] != 1:
            return False
        del points[(min_x, min_y)], points[(max_x, max_y)], points[(min_x, max_y)], points[(max_x, min_y)]
        return all(c == 2 or c == 4 for c in points.values())

s = Solution()
print(s.isRectangleCover([[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]))
