# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        res = []
        lq = [deque([root])]
        while lq:
            cur_q = lq.pop()
            tmp = deque()
            while cur_q:
                cur = cur_q.popleft()
                if not cur_q:
                    res.append(cur.val)
                if cur.left:
                    tmp.append(cur.left)
                if cur.right:
                    tmp.append(cur.right)
            if tmp:
                lq.append(tmp)
        return res
