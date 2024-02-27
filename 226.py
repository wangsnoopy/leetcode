# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # the input tree is left < root < right
        # let output become left > root > right
        # first root don't change
        # iterate all the node
        def dfs(root):
            # meet the final node
            while not root:
                return 
            left = dfs(root.left)
            right = dfs(root.right)
            root.left, root.right = root.right, root.left
        dfs(root)
        return root