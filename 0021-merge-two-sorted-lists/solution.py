# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
1,2,4 1,3,4
h->
'''
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1; cur2 = list2
        ansHead = ListNode()
        cur_ans = ansHead
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                cur_ans.next = cur1
                cur1 = cur1.next
            else:
                cur_ans.next = cur2
                cur2 = cur2.next
            cur_ans = cur_ans.next

        if not cur1:
            cur_ans.next = cur2
        if not cur2:
            cur_ans.next = cur1
        return ansHead.next

        
