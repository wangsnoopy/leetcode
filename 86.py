# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # seperate list to two list
        # 1. p.val < x, 2. p.val >= x
        dummy1, dummy2 = ListNode(), ListNode()
        p1, p2 = dummy1, dummy2
        p = head
        
        while p:
            if p.val >= x:
                p2.next = p
                p2 = p2.next
            else:
                p1.next = p
                p1 = p1.next
            # need to set a temp to cut the p list
            # or there will be a cycle of the list
            temp = p.next
            p.next = None
            p = temp
        # merge two list, p1 is now on the end of the list, so need to merge on the start of p2
        p1.next = dummy2.next
