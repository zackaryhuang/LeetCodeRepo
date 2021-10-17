from typing import List

def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    intervals.append(newInterval)
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

print(insert([[1, 5]], [2, 7]))
