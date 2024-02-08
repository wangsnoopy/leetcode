class Solution:
    def addDigits(self, num: int) -> int:
        # 0 <= num < 10
        # add until one digit
        if num < 10:
            return num
        while num >= 10:
            result = 0
            while num > 0:
                result += num % 10
                num = num // 10
            num = result
        return result