class Solution:
    def combinationSum(self, nums, target):
        dp = [0] * (target+1)
        dp[0] = 1
        for x in range(target+1):
            for y in nums:
                if x+y <= target:
                    dp[x+y] += dp[x]
        return dp[target]
