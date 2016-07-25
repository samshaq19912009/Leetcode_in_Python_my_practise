class Solution(object):
    
    def intergerBreak(self, n):
        if n == 2:
            return 1
        if n == 3:
            return 2
        res = 0
        if n % 3 == 0:
            res = 3 ** (n//3)
        if n % 3 == 1:
            res = 3 ** (n//3) * 2
        else:
            res = 3 ** (n//3 - 1) * 4
        return res




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
