# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        The idea here is to find the middle element of the sorted array 
        so that we can do a balanced tree , what ever remains to the left will go to left child and what ever remains to the right of the middle goes to right child.
        From there the left node should travel from the beginning to one place lesster than mid and right node should travel from one step above mid to the last index of the array
        [----mid----] => oth index to mid -1 for left
                      => mid+1 index to last index for right
        """
        def build_tree(left, right):
            if left > right:
                return None

            # finding middle index element of our array
            middle = (left + right) // 2

            # passing the root node by taking middle index
            node = TreeNode(nums[middle])
            # now applying the left boundary to mid -1 and mid +1 to right boundary of the array rule
            node.left = build_tree(left, middle - 1)
            node.right = build_tree(middle + 1, right)

            return node
        return build_tree(0, len(nums)-1)