# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        # we need to focust on traversing the list, checking for the value, finding the previous node of the matching node and pointing it to the next node of the matching node
        # for finding the previous node of the matching node we are going to duplicate the head and make it as a new node called dummy
        dummy = ListNode(0)
        # appending it to the head
        dummy.next = head

        # now here we are defining the additional dummy nodes so that we can go back to the previous node when we find a matching node
        previous = dummy
        current = head

        # traversing
        while current:
            if current.val == val:
                # taking the previous node and pointing it to next node
                # previous node next should be current nodes next
                previous.next = current.next
            else:
                # here when we dont need to skip current we are keeping it as previous node
                previous = current
            # moving the current to next node
            current = current.next
        # returning the original head        
        return dummy.next    
