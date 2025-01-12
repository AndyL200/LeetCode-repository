def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    n = len(intervals)
    res = 0
    intervals.sort()
    end = intervals[0][1]
    for i in range(1,n):
        if intervals[i][0] >= end:
            end = intervals[i][1]
        else:
            res += 1
            end = min(intervals[i][1], end)
    return res