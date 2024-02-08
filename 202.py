class Solution:
    def isHappy(self, n: int) -> bool:
        # loop endlessly in a cyle
        # means only meet one num per once
        # a hash map to record
        visit = set() # set can not include same element
        while n not in visit:
            visit.add(n)
            n = self.sumofSquares(n)
            if n == 1:
                return True
        return False

    def sumofSquares(self, n: int):
        # restart the result at 0
        result = 0
        while n:
            result += (n % 10) ** 2
            # renew n
            n = n // 10
        return result