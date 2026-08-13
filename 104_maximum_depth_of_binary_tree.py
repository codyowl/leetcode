# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # for empty tree
        if not root:
            return 0

        """
        The recursvie pattern to ensure the maximum depth is by getting the 
        number of layers the traversal goes.
        root -> left -> right (first layer)
        left -> left_left_child -> right_left_child(second layer)
        right -> left_right_child -> right_right_child(still second layer thats the catch)
        """
        # recursive call to get left and right depth
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        # main recursive pattern 
        return 1 + max(left_depth, right_depth)    
        