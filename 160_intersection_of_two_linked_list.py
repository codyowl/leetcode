# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # the idea here is, if we parallely visit all the object and compare it we can't find the intersection point because it wont work if both the lists are uneven, to make the uneven traversal distributed in both ways we have to follow one list entirely and switch to the other list in that way the uneven travesal will beomc distributed and both men in the intersection point if its there
        pointer_a = headA
        pointer_b = headB
        # main condition check if there is any intersection before traversal
        while pointer_a is not pointer_b:
            # checking if it is fully traversed all the nodes
            if pointer_a:
                pointer_a = pointer_a.next
            else:
                # swithching sides if the traversal fully happened
                pointer_a = headB
            if pointer_b:
                pointer_b = pointer_b.next
            else:
                pointer_b = headA
        else:
            return pointer_a         
        