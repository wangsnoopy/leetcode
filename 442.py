class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            at_index = nums[abs(num) - 1]
            # if it appear before, at_index will be negitive
            if at_index < 0:
                res.append(abs(num))
            # mark as negitive if it appear the first time
            else:
                nums[abs(num) - 1] *= -1
        
        return res
    
    # T: O(N)
    # S: O(1)