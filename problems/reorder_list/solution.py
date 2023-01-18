# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find the half and the end
        slow = fast = head
        while fast.next:
            slow = slow.next
            fast = fast.next.next
            if not fast: break

        # reverse the 2nd half
        prev, current = slow.next, None
        while prev:
            current, current.next, prev = prev, current, prev.next

        slow.next = None
        _next = head.next
        # combined them
        while _next and current:
            _next = head.next
            head.next = current
            head = head.next
            if not current: break
            current = current.next
            head.next = _next
            head = head.next