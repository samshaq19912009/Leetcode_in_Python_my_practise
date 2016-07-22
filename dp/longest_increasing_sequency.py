"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
"""

##First solution: O(n^2) complexity
##

class Solution:
    def lengthofLIS(self, nums):
        ##dp solution
        n = len(nums)
        if n == 0:
            return 0
        dp = [1 for i in range(n)]
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

    def lengthofLIS(self, nums):
        ##binary search solution
        if not nums:
            return 0
        res = []
        n = len(nums)
        res.append(nums[0])
        for i in range(1, n):
            x = nums[i]
            l, r = 0, len(res)-1
            while l<=r:
                mid = (l+r)
                if res[mid] == x:
                    l = mid
                    break
                elif res[mid] > x:
                    r = mid - 1
                else:
                    l = mid + 1
            if l >= len(res):
                res.append(x)
            else:
                res[l] = x
        return len(res)
