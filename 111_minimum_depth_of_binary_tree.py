# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # for empty node
        if not root:
            return 0
        
        # for empty left and right child that means one root node and the count is 1
        if not root.left and not root.right:
            return 1

        # now here we are ensuring if left is empty and figuring out the leaft nodes for right the reason for adding 1 is to take the current node as one count + the remaining nodes' child count
        if not root.left:
            # 1 for the current node count consideration
            return 1 + self.minDepth(root.right)

        # the same for right node
        if not root.right:
            return 1 + self.minDepth(root.left)
        # the final recursive call follows the same pattern 1 for current node count plsu the minimum of left and rith
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))        