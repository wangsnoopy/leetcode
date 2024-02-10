class Solution:
    def sumOfMultiples(self, n: int) -> int:
        sum_n = 0
        # iterate n
        for i in range(1, n+1):
            if i % 3 == 0:
                sum_n += i
            elif i % 5 == 0:
                sum_n += i
            elif i % 7 == 0:
                sum_n += i
        return sum_n