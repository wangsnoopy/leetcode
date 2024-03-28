# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # height balance: the left and right tree for every node differ in height by no more than 1
        # start from buttom
        # check if is balance or not, and record it height
        def dfs(root):
            # base case => to the leaf node
            if not root:
                return [True, 0] # return [bool, height]
            
            left, right = dfs(root.left), dfs(root.right)
            
            # check if the previous left right node is False or not, 
            # and check the current node height diff is <= 1 or not
            balanced = (left[0] and right[0] and 
                        abs(left[1] - right[1]) <= 1) # return True or False

            return [balanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]

        #T: O(n) //iterate all the node