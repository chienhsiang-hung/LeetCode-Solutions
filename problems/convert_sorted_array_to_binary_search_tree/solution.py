# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# [-10,-3,0,5,9]
# mid=(0+4)//2=2, current=0...

# Time: O(n)

# [-10,-3,0,5,9]
# mid=(0+4)//2=2, current=0, root=TreeNode(0), root.left=

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        # if len(nums) == 1:
        #     return TreeNode(nums[0])

        left, right = 0, len(nums)-1
        mid = (left+right)//2
        current = nums[mid]
        root = TreeNode(current)
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root