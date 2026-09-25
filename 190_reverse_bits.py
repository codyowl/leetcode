class Solution:
    def reverseBits(self, n: int) -> int:
        # same formula for finding the digits 
        """
        digit = number % base
        result = result * base + digit
        number //= base
        """
        result = 0
        for _ in range(32):
            digit = n % 2
            result = result * 2 + digit
            n //= 2
        return result 