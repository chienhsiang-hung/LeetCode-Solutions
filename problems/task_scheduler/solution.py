# to find how many idle we need

# n=2
# max=3
# maxct=2

# A _ _ A _ _ A
# A B _ A B _ A B
# A B idle A B idle AB

# ["A","A","A","B","B","B", "C","C","C", "D", "D", "E"]
# n=2
# max=3
# maxct=3
# A _ _ A _ _ A
# A B _ A B _ A B   now we have only 2 
# A B C A B D A B c D E

# output = max(
#     (max-1) * (n+1) + 1*maxct + (others_n - slots),
#     len(tasks)
# )
# where
#     others_n = D D E = 3
#     slots = _ _ = 2

from collections import defaultdict
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_dict = defaultdict(int)
        for t in tasks:
            tasks_dict[t] += 1
   
        # find max
        _max = 0
        for v in tasks_dict.values():
            if v > _max:
                _max = v
        # find frequence of max
        _maxct = 0
        others_n = 0
        for v in tasks_dict.values():
            if v == _max:
                _maxct += 1
            else:
                others_n += 1
        
        return max(
            (_max-1) * (n+1) + _maxct + max(others_n - max((n+1 -_maxct)*_max, 0), 0),
            len(tasks)
        )
        # Will (others_n - max((n+1 -_maxct)*_max, 0)) be negative?
        #   When slots_n > others_n
    






