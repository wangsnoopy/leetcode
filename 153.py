class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            print(l, mid, r)
            if nums[l] < nums[r]:
                return nums[l]
            if nums[mid] >= nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]