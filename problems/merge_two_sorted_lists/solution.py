# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        brute force: use an empty LinkedList to store them
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        new = ListNode()
        new_current = new
        
        current1, current2 = list1, list2
        while current1 and current2:
            if current1.val <= current2.val:
                new_current.next = ListNode(current1.val)
                new_current = new_current.next
                
                current1 = current1.next
                
            else:
                new_current.next = ListNode(current2.val)
                new_current = new_current.next
                
                current2 = current2.next
                
        # in case there is one empty
        if current1:
            new_current.next = current1
        if current2:
            new_current.next = current2
        
        return new.next