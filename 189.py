class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # revers the array first, ex k = 2 [1,2,3,4,5] become [5,4,3,2,1]
        # then seperate form the kth el to two array, and reverse them
        #[5,4] [3,2,1] => [4,5] [1,2,3]

        # if k equal to the nums lengh, then no need to reverse
        k = k % len(nums)
        l, r = 0, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1