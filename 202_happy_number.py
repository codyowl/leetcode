class Solution:
    def isHappy(self, n: int) -> bool:
        '''
        Problem statement is to separate the digits of a number , find the square of sum and keep on repeating till we reach 1, if we reach 1 thats a happy number else not
        '''
        # we are going with our familiar taking a digit and expelling pattern
        def get_next(number):
            total = 0
            while number > 0:
                # splitting it ex 19 = '1' and '9'
                digit = number % 10
                # square of sum so we need to square each numbers 1*1, 9*9
                total += digit * digit
                # now we need to expell the digit to move to next one
                number //= 10
            return total
            # here this is the second phase
            # like we saw earlier either the final number will be 1 or there are probalities that we mgiht get older number which will go on infite pattern so we returing false since if that scenario happened then its not a happy number
        visited = set()
        # doing till we reach 1
        while n != 1:
            # if its alreay part of visited then its not a happy number
            if n in visited:
                return False
            visited.add(n)
            n = get_next(n)
        return True
                
