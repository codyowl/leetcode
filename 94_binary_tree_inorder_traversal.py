# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        binary tree inorder traversal flow
        leftchildnode -> parentnode -> rightchildnode
        """ 
        result = []

        def depth_first_search(node):
            # for handling empty tree value
            if not node:
                return 

            # applying the inorder binary serach tree rule
            # left -> node -> right
            depth_first_search(node.left)
            # after traversing left we are taking the value
            result.append(node.val)
            depth_first_search(node.right)
        depth_first_search(root)
        return result      