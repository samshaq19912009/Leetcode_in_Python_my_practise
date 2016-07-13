class Solution:
    def two_sum(self, nums, target):
        dict = {}
        n = len(nums)
        for i in range(n):
            if target-nums[i] in target:
                return [dict[target - nums[i]], i]
            dict[nums[i]] = i

