class Solution:
    def hammingWeight(self, n: int) -> int:
        n = self.decimal_to_binary(n)
        count = 0
        for i in n:
            if i == '1':
                count += 1
        return count


    def decimal_to_binary(self, n):
        if n == 0:
            return "0"
        
        binary_num = ""

        while n > 0:
            remainder = n % 2
            binary_num = str(remainder) + binary_num
            n = n // 2
        
        return binary_num