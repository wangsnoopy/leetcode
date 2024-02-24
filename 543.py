# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = [0]

        def dfs(root):
            # if root is null
            if not root:
                # when root is null, it hegh is -1
                return -1
            # left and right hight
            left = dfs(root.left)
            right = dfs(root.right)
            # update the diameter
            result[0] = max(result[0], 2 + left + right)

            # hegiht of this root
            return 1 + max(left, right)

        dfs(root)
        return result[0]