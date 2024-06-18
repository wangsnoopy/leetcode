# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter = maxLeftDepth + maxRightDepth
        # Initialize the diameter to be updated during DFS
        res = [0]

        def dfs(node):
            # base case
            if not node:
                return 0

            # Recursive DFS for left and right subtrees
            left = dfs(node.left)
            right = dfs(node.right)

            # Update the diameter using current node
            res[0] = max(res[0],left + right)

            return 1 + max(left, right) # maximum depth of the given tree
        
        dfs(root)
        return res[0]