# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # bulid a list to record the show element
        check = []
        current = head
        while current is not None:
            check.append(current.val)
            current = current.next
        # check the array if it is palindrome
        check2 = check[::-1]
        return check == check2