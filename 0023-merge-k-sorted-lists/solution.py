# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
[[1,4,5],[1,3,4],[2,6]]
'''
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = []
        
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(q, (lists[i].val, i, lists[i]))
        
        dummy = ListNode()
        dest = dummy
        while q:
            _, i, cur_node = heapq.heappop(q)
            dest.next = cur_node
            dest = dest.next
            
            if cur_node.next: heapq.heappush(q, (cur_node.next.val, i, cur_node.next))
        return dummy.next
