# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
1->2->3->4->5->6->7->8->9->10
1->2->3->4->5
1->3->5->7->9

slow: 5->N

7
6->N
8
7->6
9
8->7
N
9->8

1->10->2->9->3->8->4->7->5->6
2,9
1->10
3,8
1->10->2->9

1->2->3->4
1->2
1->3
'''
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        if not slow.next: return
        pos = slow.next.next # 4; N
        mid = slow.next # 3; 3
        slow.next = None # 2->N; 2->N
        pre = slow.next # N; N
        mid.next = pre # 3->N; 3->N
        while pos:
            pre = mid # 3
            mid = pos # 4
            pos = pos.next #
            mid.next = pre # 4->3
    
        slow_next = head.next # 2; 2
        fast_next = mid.next # 9; N
        head.next = mid # 1->10; 1->3
        cur = head.next # 10; 3
        while slow_next:
            cur.next = slow_next # 10->2; 3->2
            cur = cur.next # 2; 2
            slow_next = slow_next.next # 3; N
            cur.next = fast_next # 2->9; 2->N
            cur = cur.next # 9; N
            if not fast_next: break
            fast_next = fast_next.next # 8
        
        return
            

            
            

            
        
        

