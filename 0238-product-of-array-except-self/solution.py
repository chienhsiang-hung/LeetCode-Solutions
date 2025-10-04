class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[i-1]*nums[i])
        postfix = [None] * len(nums)
        postfix[-1] = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i]
        ans = [None] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                ans[0] = postfix[1]
            elif i == len(nums)-1:
                ans[-1] = prefix[-2]
            else:
                ans[i] = prefix[i-1] * postfix[i+1]
        return ans
            
