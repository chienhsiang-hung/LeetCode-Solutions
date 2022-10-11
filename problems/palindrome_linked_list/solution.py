# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Fast and Slow runner to find the mid then start compare
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        first_half = []
        fast = slow = head
        
        # handle 1 node and 2 nodes
        if head.next is None:
            return True
        if head.next.next is None:
            return head.val == head.next.val

        while fast.next is not None:
            fast = fast.next.next

            first_half.append(slow.val)
            if fast is None:
                break
            slow = slow.next
        
        while slow.next is not None:
            slow = slow.next
            if slow.val != first_half.pop():
                return False
        return True
            

        
            
            
        