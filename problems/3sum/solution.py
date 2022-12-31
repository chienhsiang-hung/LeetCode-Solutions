class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        
        nums = sorted(nums)
        num1 = set()
        for i in range(len(nums)-2):
            if nums[i] in num1:
                continue
            num1.add(nums[i])

            l = i+1
            r = len(nums)-1

            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    output.append([ nums[i], nums[l], nums[r] ])
                    while l < r and nums[l] == output[-1][1]:
                        l += 1
                    while l < r and nums[r] == output[-1][2]:
                        r -= 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1

        return output