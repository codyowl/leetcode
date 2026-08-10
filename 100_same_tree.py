# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # checking if both are empty this is where the recursion is getting stopped
        if not p and not q:
            return True

        # if its an imbalanced child node tree
        if not p or not q:
            return False

        # main logic
        if p.val != q.val:
            return False

        # here the return will take care of the recustion 
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))        

        