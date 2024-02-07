# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # create a fake node that it next node point to the head on the linked list
        fake = ListNode(next=head)
        # two point, point prev and curr
        prev, curr = fake, head
        #while curr exist
        while curr:
            # if the val to remove, skip the curr node
            if curr.val == val:
                prev.next = curr.next
            # update the prev node to curr
            else:
                prev = curr
            # move the curr pointer forward
            curr = curr.next
        # return the next node after the fake node, which is the modified head of the list
        return fake.next