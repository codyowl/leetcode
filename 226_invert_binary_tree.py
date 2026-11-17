# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        # the idea here is to traverse and then swap left child with right and vice versa, for traversing we need to use this function as recursive

        # to ensure for empty tree
        if not root:
            return None

        # swapping
        root.left, root.right = root.right, root.left

        # doing the swapping recursively
        self.invertTree(root.left)
        self.invertTree(root.right)

        # alway return the head in case of binary tree problems
        return root