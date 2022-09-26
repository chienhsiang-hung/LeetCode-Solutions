# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_list = []
        current = head
        
        while current:
            node_list.append(current)
            
            # INCORRECT
            # i.e. len=50, this will return the final one though the middle is 25th
            # # take advantage of constraint [1, 100]
            # if len(node_list) == 50:
            #     return current
            
            current = current.next
            
        if head:
            current = node_list[len(node_list)//2]
            
        return current
        