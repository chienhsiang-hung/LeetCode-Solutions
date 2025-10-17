# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        curr = head
        slow_p = curr.next
        if not slow_p: return False
        fast_p = curr.next.next
        if slow_p == fast_p: return True
        while slow_p != fast_p:
            slow_p = slow_p.next
            if not slow_p or not fast_p.next: return False
            fast_p = fast_p.next.next
            if not fast_p: return False
        return True
