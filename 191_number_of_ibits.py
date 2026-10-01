class Solution:
    def hammingWeight(self, n: int) -> int:
        # same extract right mostbase and remove right most base % base and // base  
        count = 0
        while n > 0:
            bit = n % 2
            count += bit
            n //= 2
        return count
