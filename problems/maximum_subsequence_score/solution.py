import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        heap_list = []
        for i in range(len(nums1)):
            heap_list.append([nums2[i], nums1[i]])
            
        # new_list = sorted(new_list, key=lambda x: x[1], reverse=True)
        heapq.heapify(heap_list)

        n1_heap = []
        n2_sorted = heapq.nlargest(len(nums1), heap_list)
        for n2, n1 in n2_sorted[:k-1]:
            n1_heap.append(n1)
        heapq.heapify(n1_heap)
        
        shortlist = (
            n2_sorted[k-1][0] * ( n2_sorted[k-1][1] + (left_nlargest:=sum(n1_heap)) )
        )
        
        for i in range(k, len(nums1)):
            curr_min = n2_sorted[i][0]
            curr_v = n2_sorted[i][1]
            heapq.heappush(n1_heap, n2_sorted[i-1][1])
            left_nlargest += n2_sorted[i-1][1]
            left_nlargest -= heapq.heappop(n1_heap)
            
            shortlist = max(
                shortlist,
                curr_min * (curr_v + left_nlargest)
            )

        return shortlist