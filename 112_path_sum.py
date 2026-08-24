# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        The idea here is to take the target sum and substract it from the node value till leaf to ensure if the value is reaching 0 or not
        along the way, the target sum will be replaced with the remaining sum in our recursive call
        """
        # for empty node
        if not root:
            return False

        # main formula
        remaining_sum = targetSum - root.val

        # checking for leaf node and returning 0
        if not root.left and not root.right:
            return remaining_sum == 0

        

        return ( self.hasPathSum(root.left, remaining_sum) or
                 self.hasPathSum(root.right, remaining_sum) )   