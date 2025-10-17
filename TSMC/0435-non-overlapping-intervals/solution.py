class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        curr = intervals[0]
        ans = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] < curr[1]:
                ans += 1
                continue
            curr = intervals[i]
        return ans
