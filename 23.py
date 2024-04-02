# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # let ListNode can be compared
        ListNode.__lt__ = lambda self, other: self.val < other.val
        # Define a heap to store the nodes
        heap = []
    
        # Push the head of each linked list to the heap
        for head in lists:
            if head:
                # since define __lt__, so just need to put head inside
                heapq.heappush(heap, head)
    
        # Create a dummy node to simplify the code
        dummy = ListNode(0)
        cur = dummy
    
        # Continue until all nodes are processed
        while heap:
            # Pop the node with the smallest value from the heap
            node = heapq.heappop(heap)
        
            # Append the popped node to the result list
            cur.next = node
            # update cur node
            cur = cur.next
        
            # Move the pointer of the popped node to the next node in its list
            if node.next:
                heapq.heappush(heap, node.next)
    
        # Return the merged list (starting from the next of the dummy node)
        return dummy.next
