class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height) - 1
        left, right = 0, n
        result = 0
        # iterate all the point
        while left < right:
            # get max area
            current = min(height[left], height[right]) * (right - left)
            result = max(result, current)
            # update the point
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return result