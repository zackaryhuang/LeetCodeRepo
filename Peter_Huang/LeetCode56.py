
# 56. 合并区间
# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。

#  

# 示例 1：

# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 示例 2：

# 输入：intervals = [[1,4],[4,5]]
# 输出：[[1,5]]
# 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
#  

# 提示：

# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104

from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x:x[0])
    for i in range(1, len(intervals)):
        left = intervals[i][0]
        right = intervals[i][1]
        lastLeft = intervals[i-1][0]
        lastRight = intervals[i-1][1]
        if left <= lastRight:
            intervals[i-1][1] = max(lastRight, right)
            intervals[i] = intervals[i-1]
    returnIntervals = []
    for interval in intervals:
        if interval not in returnIntervals:
            returnIntervals.append(interval)

    return returnIntervals
        


print(merge([[1,4],[0,4],[2,2]]))