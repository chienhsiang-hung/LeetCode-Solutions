class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        # O(n^2)
        global_max = 0
        for i in range(len(colors)-1):
            local_max = len(colors)-i-1
            for j in range(len(colors)-1, i, -1):
                if colors[i] != colors[j]:
                    if local_max > global_max:
                        global_max = local_max
                        break
                local_max -= 1
        return global_max