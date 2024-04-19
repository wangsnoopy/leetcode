"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        self.traverse(root.left, root.right)
        return root

    def traverse(self, node1, node2):
        if not node1 and not node2:
            return None
        # connect the node
        node1.next = node2

        #connect the node with same parents
        self.traverse(node1.left, node1.right)
        self.traverse(node2.left, node2.right)

        # connect the node with different parents
        self.traverse(node1.right, node2.left)