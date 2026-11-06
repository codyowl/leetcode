# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        # the idea here is to reverse the linked list like how we do a string/list reversal, similar to negative indexing[::-1] we need to traverse the final node
        # take the next node -> save it in a temp -> next should point to previous which should be None initially -> previous should be current -> current should be next 
        previous = None
        current = head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
            # thats it thats a full cycle there similar to negative indexing
        # previous will become the head now
        return previous     

        
        