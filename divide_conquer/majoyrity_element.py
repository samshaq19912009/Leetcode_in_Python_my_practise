class Solution:
    def majority(self, nums):
        res, cnt = 0, 0
        for num in nums:
            if res == num:
                cnt += 1
            elif cnt:
                cnt -= 1
            else:
                cnt = 1
                res = num
        return res

