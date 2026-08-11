# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_mirror(left_node, right_node):
            """
            Idea here is to check if left side of a node is equal to right side 
            """

            # checking if the positions of both nodes are empty
            if not left_node and not right_node:
                return True

            # checking if one of them is empty
            if not left_node or not right_node:
                return False

            # mirrored position values differ
            if left_node.val != right_node.val:
                return False

            return (
                is_mirror(left_node.left, right_node.right) and \
                is_mirror(left_node.right, right_node.left)
            )
        return is_mirror(root.left, root.right)