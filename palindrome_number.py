class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:    
            number = x
            reverse = 0
            while x:
                # taking the last digit
                digit = x % 10 
                # adding it to reverse
                reverse = reverse * 10 + digit
                # removing the last digit
                x = x // 10
            if number == reverse:
                return True
            
         

s = Solution()
print s.isPalindrome(121)                