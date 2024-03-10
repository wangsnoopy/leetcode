import heapq
import collections
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # how long take signal to visit every node

        # create a defaultdict to store the adjancey list representation of the graph
        edges = collections.defaultdict(list)

        # Populate the adjaceny list with the given edges and weights
        for u, v, w in times:
            edges[u].append((v, w))
        
        # Initialize a minHeap with (0, k), where k is the starting node and 0 is the cost to k
        minHeap = [(0, k)]

        # Initialize a set to keep track of visited node
        visit = set()

        # Initialize the time variable to track the maxium time taken to reach out all node
        t = 0

        # While there are element in the minHeap
        while minHeap:
            # Pop the node with the minimum distance from the minHeap
            travel_time, node = heapq.heappop(minHeap) # first, travel_time = 0, node = k

            # If the node has been visited, continue to the next iteration
            if node in visit:
                continue
            # Mark the current node as visited
            visit.add(node)
            
            # update the time to the current distance
            t = travel_time

            # Iterate over the neighbors of the current node
            for neighbor, travel_time_neighbor in edges[node]:
                # If the neighbor has not been visited yet
                if neighbor not in visit:
                    # Add the neighbor to the minHeap with updated distance
                    heapq.heappush(minHeap,(travel_time + travel_time_neighbor, neighbor))
        # If all nodes have been visited, return the maxium time taken
        return t if len(visit) == n else -1