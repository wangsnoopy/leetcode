class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # need strictly increasing and strictly decreasing
        # check if it is strictly increase and decrease
        if len(arr) < 3:
            return False
        l, r = 0, 1
        # check increase, meet the top
        while arr[l] < arr[r]:
            if arr[l] == arr[r]:
                return False
            elif r == len(arr) - 1:
                return False
            l += 1
            r += 1
        #then check decrease
        while r < len(arr):
            # always decreasing
            if l == 0:
                return False
            if arr[l] == arr[r]:
                return False
            elif arr[l] < arr[r]:
                return False
            l += 1
            r += 1
        return True