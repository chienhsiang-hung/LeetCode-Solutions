class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left = []
        right = []
        for interval in intervals:
            if interval[0] < newInterval[0]:
                left.append(interval)
            elif interval[0] > newInterval[0]:
                right.append(interval)
            # interval[0] == newInterval[0]
            elif interval[1] < newInterval[1]:
                left.append(interval)
            elif interval[1] > newInterval[1]:
                right.append(interval)
            else:
                return intervals
            
        intervals = left + [newInterval] + right
        new_output = [intervals[0]]
        last = intervals[0]
        for interval in intervals[1:]:
            if interval[0] > last[1]:
                new_output.append(interval)
            
            # delete interval[0]
            else:
                if interval[1] <= last[1]:
                    continue
                else:
                    new_output[-1][1] = interval[1]
            
            last = new_output[-1]
        
        return new_output