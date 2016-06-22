class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0:
            return 0
        dp = [0 for i in range(n)]
        dp[0] = 0
        for i in range(1,n):
            dp[i] = max(dp[i-1], dp[i-1] + prices[i] - prices[i-1])

        return dp[-1]
