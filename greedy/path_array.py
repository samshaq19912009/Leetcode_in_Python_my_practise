"""
Given a sorted positive integer array nums and an integer n, add/patch elements to the array such that any number in range [1, n] inclusive can be formed by the sum of some elements in the array. Return the minimum number of patches required.

Example 1:
nums = [1, 3], n = 6
Return 1.
"""

class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        idx, total, ans = 0, 1, 0
        size = len(nums)
        while total <= n:
            if idx < size and nums[idx] <= total:
                total += nums[idx]
                idx += 1
            else:
                total <<= 1
                ans += 1
        return ans
