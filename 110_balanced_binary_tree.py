# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_height(node):
            """
            The idea here is to use the format to find maximum depth of a tree
            which is 
            return 1 + max(left_depth, right_depth)    
            """
            
            # checking if the node doesn't have any child tree
            if not node:
                return 0

            # checking recursively left child
            left_height = check_height(node.left)
            if left_height == -1:
                return -1

            # checking recursively right child 
            right_height = check_height(node.right)
            if right_height == -1:
                return -1 

            # no the thumb rule left - right > 1
            if abs(left_height - right_height) > 1:
                return -1

            # now here we are using our reuasble pattern to find depth of a tree
            return 1 + max(left_height, right_height)    
        # after getting final value we have to determine whether its balancer or nto with the return value as not -1
        return check_height(root) != -1
