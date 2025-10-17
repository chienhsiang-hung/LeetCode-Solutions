# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None

        s = head.next
        if not head.next: return None
        f = head.next.next
        while f and f.next:
            if s == f: # there is a cycle
                f = head
                while s != f:
                    s = s.next
                    f = f.next
                return s
            s = s.next
            f = f.next.next
        
        return None
