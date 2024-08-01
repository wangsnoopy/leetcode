class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of the sequence
            # if n have no neighbor n-1, then it's the start
            if (n - 1) not in numSet:
                # find the start point
                length = 1
                while (n + length) in numSet:
                    length += 1
                # update max legth
                longest = max(length, longest)
        
        return longest