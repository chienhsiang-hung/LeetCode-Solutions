class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        right = left = 0
        window = defaultdict(int)
        pairs_count = defaultdict(int)
        ans = 0
        while left < len(nums)-1:
            # extend window
            if right < len(nums):
                window[nums[right]] += 1
                if window[nums[right]] >= 2:
                    pairs_count[nums[right]] += window[nums[right]]-1

            while sum([v for v in pairs_count.values()]) >= k:
                ans += len(nums)-right if len(nums)-right else 1
                # shrink window
                window[nums[left]] -= 1
                if window[nums[left]] >= 1:
                    pairs_count[nums[left]] -= window[nums[left]]
                left += 1
                continue

            if right < len(nums):
                right += 1
            else:
                left += 1
        return ans