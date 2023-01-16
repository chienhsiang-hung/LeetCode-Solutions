class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles = sorted(piles)

        def empty_all_time(k):
            '''
            @k: eating speed
            @return: bool of if the banana can be empty with the k-speed
            '''
            hh = 0
            for p in piles:
                hh += p // k
                if p % k > 0:
                    hh += 1
            return hh

        min_eating_speed = piles[-1]
        l, r = 1, piles[-1]
        while l <= r:
            k = (l+r)//2
            if (
                hh := empty_all_time(k)
            ) <= h:
                min_eating_speed = min(min_eating_speed, k)
                r = k-1
            else:
                l = k+1

        return min_eating_speed