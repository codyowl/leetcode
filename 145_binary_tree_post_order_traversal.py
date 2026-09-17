# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        # post order is similar to pre order except the flow should be like this visit left child -> right child -> current node
        result = []
        def dfs(node):
            if not node:
                return
            # visiting left subtree
            dfs(node.left)
            # visiting right subtree
            dfs(node.right)
            # appending the current node
            result.append(node.val)
        # recursively traversing the ndoes
        dfs(root)
        return result        

    
        