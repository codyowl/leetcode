# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        result = list()
        # pre order traversal rule is node -> left child -> right child
        def dfs(node):
            
            # handling empty
            if not node:
                return
            result.append(node.val)
            # visiting left child
            dfs(node.left)
            # visiting right child
            dfs(node.right)
        # travesing from root
        dfs(root)
        return result    

        