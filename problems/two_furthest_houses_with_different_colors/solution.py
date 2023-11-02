class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        # O(n)
        if colors[0] != colors[len(colors)-1]:
            return len(colors)-1
        
        my_max = 0
        for i in range(1, len(colors)):
            if colors[i] != colors[0]:
                my_max = max(
                    my_max, max(i-0, len(colors)-i-1)
                )                

        return my_max
            