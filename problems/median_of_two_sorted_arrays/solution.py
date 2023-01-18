class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        _len = len(nums1) + len(nums2)
        if len(nums1) > len(nums2): # let nums1 be the short one
            nums1, nums2 = nums2, nums1

        mid1 = len(nums1) // 2
        while True:
            mid2 = (_len+1) // 2 - mid1 -1
            if (
                1 <= mid1 <= len(nums1) and
                0 <= mid2+1 < len(nums2) and
                nums1[mid1-1] > nums2[mid2+1]
            ):
                mid1 -= 1
            elif (
                0 <= mid1 < len(nums1) and 
                0 <= mid2 < len(nums2) and
                nums2[mid2] > nums1[mid1]
            ):
                mid1 += 1
            
            # found the partition
            else:
                lu = nums1[mid1-1] if 1 <= mid1 <= len(nums1) else -(10**6)
                ld = nums2[mid2] if 0 <= mid2 < len(nums2) else -(10**6)
                ru = nums1[mid1] if 0 <= mid1 < len(nums1) else 10**6
                rd = nums2[mid2+1] if 0 <= mid2+1 < len(nums2) else 10**6
                if _len % 2 == 1:
                    return max(lu, ld)
                return ( max(lu, ld) + min(ru, rd) ) /2
            
