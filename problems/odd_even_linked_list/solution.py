# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # len(Node) == 0
        if not head:
            return None
        odd = ListNode(head.val)
        head_odd = odd
        # len(Node) == 1
        if not head.next:
            return odd
        flag = 2
        even = ListNode(head.next.val)
        head_even = even

        current = head.next.next
        while current:
            flag += 1
            # odd
            if flag%2 == 1:
                odd.next = ListNode(current.val)
                odd = odd.next
            else:
                even.next = ListNode(current.val)
                even = even.next
            current = current.next
            
        odd.next = head_even
        return head_odd