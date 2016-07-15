class Solution:
    def two_sum(self, nums, target):
        dict = {}
        n = len(nums)
        for i in range(n):
            if target-nums[i] in target:
                return [dict[target - nums[i]], i]
            dict[nums[i]] = i

    #what if the data has already been sored in ascending order???
    
    def two_sum_2(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l < r:
            tmp = nums[l] + nums[r]
            if tmp == target:
                return [l,r]
            elif tmp > target:
                r -= 1
            else:
                l += 1
                
        return []
