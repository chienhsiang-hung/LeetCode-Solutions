class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-4, -1, -1, 0, 1, 2]
        nums.sort()
        
        ans = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i+1
            k = len(nums) -1
            while j < k:
                if j > i+1 and nums[j] == nums[j-1]:
                    j += 1
                    continue
                if k < len(nums)-1 and nums[k] == nums[k+1]:
                    k -= 1
                    continue

                if (total := nums[i] + nums[j] + nums[k]) == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1
        return ans
