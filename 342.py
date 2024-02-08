class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # less than 0 and equal 0 always be false
        if n <= 0:
            return False
        # check if can be divide by 4
        while n % 4 == 0:
            n /= 4
        # divide at the end will be 1
        return n == 1