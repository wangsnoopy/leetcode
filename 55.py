class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)
        step = nums[0]
        for i in range(1, n):
            if step == 0:
                return False
            step -= 1
            # update the current max step
            step = max(step, nums[i])
        return True