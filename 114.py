# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # base case
        if not root:
            return None
        
        # flat the left right root
        self.flatten(root.left)
        self.flatten(root.right)

        left = root.left
        right = root.right

        # let the left root be on the right root
        root.left = None
        root.right = left

        # paste the right root on the end of the current right root
        p = root
        while p.right:
            # to the end of the current right root
            p = p.right
        p.right = right