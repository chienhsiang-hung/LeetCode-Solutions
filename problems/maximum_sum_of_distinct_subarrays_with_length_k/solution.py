from collections import defaultdict, deque

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        if k > len(nums):
            return 0
        
        window = deque()
        window_dict = defaultdict(int)
        # not_distinct = False
        # local_max = 0
        # for j in range(k):
        #     window_dict[nums[j]] += 1
        #     if window_dict[nums[j]] == 1:
        #         window.append(nums[j])
        #         local_max += nums[j]
        #     else:
        #         not_distinct = True
        #         break
        # if not not_distinct:
        #     max_sum = local_max
        # else:
        #     max_sum = 0
        
        max_sum = 0
        local_sum = 0
        valid = 0
        false_num = 0
        true_num = 0
        for i in range(len(nums)):
            if i >= k:
                if window.popleft() == False:
                    false_num -= 1
                window_dict[nums[i-k]] -= 1
                local_sum -= nums[i-k]
            local_sum += nums[i]
            window_dict[nums[i]] += 1
            if window_dict[nums[i]] == 1:
                window.append(True)
                if true_num < k:
                    true_num += 1
            else:
                window.append(False)
                false_num += 1
            if (false_num == 0 or (false_num==1 and not window[0])) and true_num == k:
                if local_sum > max_sum:
                    max_sum = local_sum
        return max_sum

            
#         window_dict = defaultdict(int)            
                    
#         for i in range(len(nums)-k):
            
            
#             window = defaultdict(int)
#             local_max = 0
#             not_distinct = False
#             for j in range(k):
#                 window[nums[i+j]] += 1
#                 if window[nums[i+j]] == 1:
#                     local_max += nums[i+j]
#                 else:
#                     not_distinct = True
#                     break
#             if not_distinct:
#                 continue
#             else:
#                 if local_max > max_sum:
#                     max_sum = local_max
#         return max_sum