# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # let the node.val become the node.next.val(4,5,1,9 >> 4,1,1,9)
        node.val = node.next.val
        # let the node print to the next.next node, it means we remove the node.next not the node
        # (4>1>1>9 4>1 1 >9)
        #             --->
        node.next = node.next.next