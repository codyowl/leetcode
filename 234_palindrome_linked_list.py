# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        # the idea here it to implement the thumb rule in palindrome which is mylist == mylist[::-1] we can convert the singly linked list to a list to achieve this despite this wont be a O(1) solution
        mylist = list()
        # taking the head and assign it to a value
        current = head
        # now here we need to move to each element while appending the element to our list
        while current:
            mylist.append(current.val)
            # moving to next element
            current = current.next
        # returning true if the palnidrome exists
        return mylist == mylist[::-1]