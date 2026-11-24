class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # the idea here is to check if the given number can be a power of two by keep on dividing it until reaching the last level, if the last level is an odd number then its not a power of two else it is
        # the number should not be negative
        if n <= 0:
            return False
        while n > 1:
            # here we need to ensure if the modulo diving is giving 0
            if n % 2 != 0:
                return False
            # taking the given number to each level by keep on diving it until reachidn last
            n = n // 2
        # if it comes until this then its a power of two    
        return True