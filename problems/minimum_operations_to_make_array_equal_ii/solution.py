class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # find diff
        diffs = set()
        for i in range(len(nums1)):
            if nums1[i] != nums2[i]:
                diffs.add(i)
        
        # edge case                
        if k == 0 and diffs:
            return -1
        

        to_sub = to_add = 0
        for i in diffs:
            if (local_diff:=nums1[i] - nums2[i]) % k != 0:
                return -1

            if nums1[i]>nums2[i]:
                to_sub += abs(local_diff / k)
            elif nums1[i]<nums2[i]:
                to_add += abs(local_diff / k)

        if to_sub != to_add:
            return -1
        return int(to_sub)
            
            
            
     
                
                
            
        
        
                