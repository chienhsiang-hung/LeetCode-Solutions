# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


### Simulation Process ###
# [4-> 2-> 1-> 3]

# 4, 4-> 1, 2-> None, 1
# l, r = sort(4->1), sort(3)

# sort(3)
# [3]

# sort(4->1)
# [4-> 2-> 1]

# 4, 4-> 1, 2
# l, r = sort(1->2), sort(None)
###########################
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # use two pointer to find the mid point for Merge Sort
        fast = slow = head
        while fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if not fast.next:
                break
        start = slow.next
        slow.next = None
        l, r = self.sortList(head), self.sortList(start)

        return self.merge(l, r)
    
    def merge(self, l, r):
        if not l or not r:
            return l or r
        head = tmp = ListNode(0)
        while l and r:
            if l.val <= r.val:
                tmp.next = l
                l = l.next
            else:
                tmp.next = r
                r = r.next
            tmp = tmp.next
        if l:
            tmp.next = l
        if r:
            tmp.next = r
        return head.next
            