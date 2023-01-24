# example
#   [1,2,1,2,1], k=2

###### integrate this process to dp to accelerate (stay away from TLE)######
# record all trim_lens first
#   trim_lens[0][0] is for nums[0:1]
#   trim_lens[1][1] is for nums[1:2]
#   trim_lens[4][4] is for nums[4:5]

        # trim_lens = [
        #     [0] * len(nums) for _ in range(len(nums))
        # ]

        # for i in range(len(nums)):
        #     current_tri_len = 0
        #     num_cnt = Counter()
        #     for j in range(i, len(nums)):
        #         num_cnt[nums[j]] += 1
        #         if num_cnt[nums[j]] == 2:
        #             current_tri_len += 2
        #         elif num_cnt[nums[j]] > 2:
        #             current_tri_len += 1

        #         trim_lens[i][j] = current_tri_len
###### integrate this process to dp to accelerate (stay away from TLE)######

class Solution:
    def minCost(self, nums: List[int], k: int) -> int:

        # dp starts w/ memoization
        @cache
        def dp(k, i):
            if i == len(nums): return 0

            cost = float('inf')
            n_cnt = Counter()
            trim_len = 0
            for j in range(i, len(nums)):
                n_cnt[nums[j]] += 1
                if n_cnt[nums[j]] == 2:
                    trim_len += 2
                elif n_cnt[nums[j]] > 2:
                    trim_len += 1

                cost = min(
                    cost,
                    trim_len + k + dp(k, j+1)
                )
            return cost
        
        return dp(k, 0)