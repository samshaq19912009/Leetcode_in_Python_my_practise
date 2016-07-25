class Solution(object):

    def integerBreak(self, n):

        if n == 2:
            return 1
        if n == 3:
            return 2
        dp = [1 for x in range(n+1)]
        dp[2] = 2
        dp[3] = 3
        for i in range(4, n+1):
            dp[i] = max(dp[i-2]*2, dp[i-3]*3)

        return dp[n]
