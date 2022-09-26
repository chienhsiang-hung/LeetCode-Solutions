# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Assume there is no duplicated node val.
        '''
        if not head:
            return None
        
        fast = slow = head
        loop = False
        while fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                loop = True
                break
            if not fast:
                return None

        if not loop:
            return None

        fast = head
        while fast:
            if slow == fast:
                return slow
            fast = fast.next
            slow = slow.next
