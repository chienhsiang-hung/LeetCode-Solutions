# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        temp_output = deque()
        pre_level = 0
        queue = deque([(root, pre_level)])
        while queue:
            current, level = queue.popleft()

            # if the level changed
            if level > pre_level:
                # record the list
                output.append(temp_output)
                pre_level = level
                temp_output = deque()

            if current and (
                level%2 == 0
            ):
                temp_output.append(current.val)
            elif current:
                temp_output.appendleft(current.val)
            elif not current:
                break

            # append to queue
            if current.left:
                queue.append((current.left, level+1))
            if current.right:
                queue.append((current.right, level+1))
        if temp_output:
            output.append(temp_output)

        return output