class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        # iterate all the point
        for num in nums:
            # maintan the heap size, only puting k element in the heap
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                # heap[0] is the smallest number in the min heap
                if num > heap[0]:
                    # pop the smallest element of the heap
                    heapq.heappop(heap)
                    # add the larger number to the heap
                    heapq.heappush(heap, num)
        return heap[0]

    # T: N * log K
    # S: O(K)

    # Quickselect method(don't use)
    # T: O(N) -> O(n^2) (worest case)
    # S: O(1)