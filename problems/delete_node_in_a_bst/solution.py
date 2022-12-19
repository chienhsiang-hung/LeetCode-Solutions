# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # find the node to delete
        current = root
        left_child = True
        parent = None
        while current:
            if current.val > key:
                parent = current
                current = current.left
                left_child = True
            elif current.val < key:
                parent = current
                current = current.right
                left_child = False
            else:
                break
        if not current: return root # when no deletion needs to be done
            
        
        if not current.left and not current.right:
            if not parent: return None # when the root is [key] only
            if left_child:
                parent.left = None
            else:
                parent.right = None
        elif not current.left and current.right:
            if not parent: return current.right
            if left_child:
                parent.left = current.right
            else:
                parent.right = current.right
        elif current.left and not current.right:
            if not parent: return current.left
            if left_child:
                parent.left = current.left
            else:
                parent.right = current.left
        else:
            # find the smallest in the right
            right_tree_parent = current
            right_tree = current.right
            if right_tree.left:
                while right_tree.left:
                    if right_tree.left:
                        right_tree_parent = right_tree
                        right_tree = right_tree.left
                current.val = right_tree.val # swap the val
                # delete the last one after the exchange or add the right of the rest
                right_tree_parent.left = right_tree.right
                
            
            # combine the right directly
            else:
                right_tree.left = current.left
                if not parent: return right_tree

                if left_child:
                    parent.left = right_tree
                else:
                    parent.right = right_tree
                        
        return root