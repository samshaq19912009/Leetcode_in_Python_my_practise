class Solution:
    def maxSubArray(self, nums):
        ##不是用DP并不合适，因为dp[n]有可能会依赖之前的subarray状态！！！！
        n = len(nums)

        if n < 2:
            return nums[0]

        ans, tmp = nums[0], nums[0]

        for i in range(1,n):
            tmp = max(tmp+nums[0], nums[0])
            ans = max(ans, tmp)


        return ans
