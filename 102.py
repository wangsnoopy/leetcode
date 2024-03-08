# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        # create a queue
        q = collections.deque()
        # first add the given root
        q.append(root)

        # start running the BFS
        while q: # if queue is empty, then all node is done
            qLen = len(q)
            level = []
            # iterate all the node in queue
            for i in range(qLen):
                node = q.popleft() # first in first out
                if node:
                    level.append(node.val)
                    # add the node child
                    q.append(node.left)
                    q.append(node.right)
            # after iterate the current level all nodes
            if level: # child may be empty
                res.append(level)
        return res