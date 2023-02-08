# [10,9,2,5,3,4]
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for i, n in enumerate(nums):
            if i == 0 or n > sub[-1]:
                sub.append(n)
            else:
                l, r = 0, len(sub)-1
                while True:
                    mid = (l+r) // 2
                    if (
                        (mid >= 1 and sub[mid] > n > sub[mid-1]) or
                        (mid == 0 and sub[mid] > n)
                    ):
                        sub[mid] = n
                        break

                    if sub[mid] < n:
                        l = mid +1
                    elif sub[mid] > n:
                        r = mid -1
                    else:
                        sub[mid] = n
                        break
        return len(sub)