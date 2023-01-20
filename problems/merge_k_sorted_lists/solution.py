# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# divide and conquer
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return ListNode().next
        if len(lists) == 1: return lists[0]

        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        return self.merge(left, right)
        
    
    def merge(self, left, right):
        head = ListNode()
        current = head
        while left or right:
            if left and right:
                if left.val < right.val:
                    current.next = left
                    left, current = left.next, current.next
                else:
                    current.next = right
                    right, current = right.next, current.next
            elif left:
                current.next = left
                break
            else:
                current.next = right
                break
        return head.next

        
        