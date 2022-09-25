# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        brute force: store it in a list and create a new Linked List
        time: O(N)
        space: O(1)
        '''
        from collections import deque
        new_list = deque()
        current = head
        while current:
            new_list.appendleft(current.val)
            current = current.next
            
        new_ll = ListNode()
        current_ll = new_ll
        while new_list:
            current_ll.next = ListNode(new_list.popleft())
            current_ll = current_ll.next
        
        return new_ll.next
        
            
            
        