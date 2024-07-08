# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root

        # iterative in-order DFS traversal
        while cur or stack:
            while cur: # go as left as possible
                stack.append(cur)
                cur = cur.left 
            
            cur = stack.pop() # last one, smallest node
            n += 1
            if n == k:
                return cur.val
            
            cur = cur.right