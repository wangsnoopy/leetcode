class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # return a lsit of all MHT's root labels
        # if only 1 node, return [0]
        # if 2 node, both node is MHT's root, since both height are 1, return [A,B]
        # GOAL 
        # 1. pop the leaf of the tree (leaf to leaf is the longest dist, so leaf can't be MHT's root)
        # 2. if there is only 1 or 2 node, then here is the answer

        # Base case
        if n <= 2:
            return [x for x in range(n)]

        # make the graph, need to record each node connection
        # EDGEs: [[1,0],[1,2],[1,3]]
        # GRAPH: 
        # node:         [0,     1,    2,  3]
        # connect node: [{1},{0,2,3},{1},{1}]]

        # forming the graph
        # create a list record the connect node
        neighbors = [set() for x in range(n)]

        for start, end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)
        
        # initialize the first layer of leaves
        leaves = []
        for i in range(n):
            if len(neighbors[i]) == 1:
                leaves.append(i)

        # keep remove leaves until reach the center
        remaining_node = n # n nodes

        # if node nums is <= 2, then we meet the center
        while remaining_node > 2:
            remaining_node -= len(leaves)
            temp = []

            # remove the leaf in each node connection
            for leaf in leaves: # leaves = [0,2,3]
                for neighbor in neighbors[leaf]: # neighbors[0] = {1}
                    neighbors[neighbor].remove(leaf)
                    
                    # update the new leaves
                    if len(neighbors[neighbor]) == 1:
                        temp.append(neighbor)
            leaves = temp
        
        return leaves