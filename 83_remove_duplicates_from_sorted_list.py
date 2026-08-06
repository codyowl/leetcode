# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_place = head

        while current_place and current_place.next:
            # since its a sorted linked list the duplicate value will be near by
            if current_place.val == current_place.next.val:
                # here we are ensuring to skip the next element in list if the value is same as previous and marking the next pointer to the element next to it
                current_place.next = current_place.next.next
            else:
                # when no matching successor found simply point to next
                current_place = current_place.next

        return head    