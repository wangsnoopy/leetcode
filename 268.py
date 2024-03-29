class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # sort the array
        nums.sort()
        index = 0
        # print(index, nums)
        while index < len(nums):
            if nums[index] == index:
                index += 1
            else:
                return index
        return index