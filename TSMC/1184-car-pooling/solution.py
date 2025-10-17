'''
[[2,1,5], [3,3,7]], 4
...
'''
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pOnLocations = [0] * 1001
        for p, f, t in trips:
            pOnLocations[f] += p
            pOnLocations[t] -= p

        if pOnLocations[0] > capacity: return False
        for i in range(1, len(pOnLocations)):
            pOnLocations[i] += pOnLocations[i-1]
            if pOnLocations[i] > capacity:
                return False
        return True
