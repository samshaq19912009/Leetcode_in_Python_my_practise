class Solution:
    def 3_sum_close(self, nums, target):
        n = len(nums)
        min_gap = 10000
        result = 0
        nums.sort()

        for i in range(n-2):
            j = i+1
            k = n-1
            while j < k:
                tmp = nums[i]+nums[j]+nums[k]
            
                gap = abs(target - tmp)
                if gap < min_gap:
                    min_gap = gap
                    result = tmp
            
                if tmp < target:
                    j += 1
            
                else:
                    k -= 1
            
                
        return ans
