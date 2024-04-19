class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # set maxSun to -inf
        maxSum =float(-inf)
        currentSum = 0

        # iterate the array
        for num in nums:
            currentSum += num

            # update maxSum with the new value of currentSum. found a new maximum subarray sum.
            if currentSum > maxSum:
                maxSum = currentSum
            
            # indicates that including the current element in the subarray would reduce the overall sum
            # start a fresh subarray
            if currentSum < 0:
                currentSum = 0
        
        return maxSum