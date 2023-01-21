class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if nums1[0] < nums2[0]:
            nums1, nums2 = nums2, nums1
        
        visited = defaultdict(bool)
        for n2 in nums2:
            visited[n2] = True
        
        for n1 in nums1: # bigger
            if n1 > nums2[-1]:
                break
            if visited[n1]:
                return n1
            
        return -1