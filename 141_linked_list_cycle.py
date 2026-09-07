# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # the idea here is to have one set to make the find operation faster instead of a list and visiting every node and append it and while traversing have to ensure if the node has been part of the set or not
        visited = set()
        current = head
        while current:
            if current in visited:
                return True
            visited.add(current)
            # traversing to next node    
            current = current.next
        # after making entire iteration when there is no such visisted conditions there are no cycle    
        return False    
        