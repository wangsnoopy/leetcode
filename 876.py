# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # initialize two pointers i, j point to head
        i, j = head, head

        # move j two step forward, i one step
        while j != None and j.next != None:
            i = i.next
            j = j.next.next
        
        return i