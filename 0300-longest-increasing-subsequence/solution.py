class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            local_best = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    local_best = max(local_best, dp[j]+1)
            dp[i] = local_best
        return max(dp)
