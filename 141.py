# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # using two pointer
        slow, fast = head, head

        while fast and fast.next:
            # one point the next one, another point to the next two one
            slow = slow.next
            fast = fast.next.next
            # if two pointer meet, that means there is a cycle
            if slow == fast:
                return True

        return False