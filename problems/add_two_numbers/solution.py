# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tail = ListNode()
        current = tail
        n = 0
        while l1 or l2 or n:
            if l1:
                n += l1.val
                l1 = l1.next
            if l2:
                n += l2.val
                l2 = l2.next
            
            current.next = ListNode(n%10)
            n = n//10
            current = current.next
        return tail.next
            
            
            
