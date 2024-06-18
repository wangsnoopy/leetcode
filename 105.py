# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        # Recursively build the left subtree using the left part of preorder and inorder lists.
        root.left = self.buildTree(preorder[1:index + 1], inorder[:index])
        # Recursively build the right subtree using the right part of preorder and inorder lists.
        root.right = self.buildTree(preorder[index + 1:], inorder[index + 1:])
        return root

#O(n^2) >> for each node find index O(n), recursive n node >> n^2