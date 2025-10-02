# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        1>2>3>4>5
            pre=None curr=1 next=2, 1>None
            pre=1 curr=2 next=3, 2>1
        '''
        if not head: return None
        pre = None
        curr = head
        next_node = curr.next
        curr.next = pre
        while next_node:
            pre = curr
            curr = next_node
            next_node = next_node.next
            curr.next = pre
        return curr
