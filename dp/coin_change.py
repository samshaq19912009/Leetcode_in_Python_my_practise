class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        INT_MAX = 21454456
        dp = [INT_MAX] * (amount+1)
        dp[0] = 0
        for x in range(amount):
            if dp[x] == INT_MAX:
                continue
            for c in coins:
                if x + c > amount:
                    continue
                dp[x+c] = min(dp[x+c], dp[x]+1)
        if dp[amount] == INT_MAX:
            return -1
        return dp[amount]
