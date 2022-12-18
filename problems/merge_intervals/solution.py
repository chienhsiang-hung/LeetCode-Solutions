class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the input first
        intervals = sorted(intervals, key=(lambda x: x[0]))

        output = [intervals[0]] # add the first ele
        last = intervals[0]
        for interval in intervals[1:]:
            if interval[0] > last[1]:
                output.append(interval) # add new interval
            
            else: # delete the interval[0]
                if interval[1] >= last[1]:
                    output[-1][1] = interval[1] # change to new interval[1]
                else:
                    continue # do nothing
            last = output[-1]
        return output