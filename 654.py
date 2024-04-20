# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # base case
        if not nums:
            return None
        # find the max num, and index
        maxNum = max(nums)
        maxIndex = nums.index(maxNum)

        # set the maxNum as the tree root
        root = TreeNode(maxNum)

        # define the left, right root
        # subarray prefix
        root.left = self.constructMaximumBinaryTree(nums[:maxIndex])
        # subarray suffix
        root.right = self.constructMaximumBinaryTree(nums[maxIndex+1:])

        return root