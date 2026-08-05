class Solution:
    def climbStairs(self, n: int) -> int:
        # dynammic programmind 1d 
        dp = [0] * (n + 1)

        # adding condition for less than 2
        if n < 2:
            return n

        # cause we know these two ways
        dp [1] = 1
        dp [2] = 2

        # starding from the index 3 because we know the value of 1 and 2
        for i in range(3, n+1):
            # main dp formula 
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]    