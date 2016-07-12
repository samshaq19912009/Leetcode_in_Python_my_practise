"""
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""

class Solution:
    def search_range(self, nums, target):
        n = len(nums)
        l = self.binarySearch(nums, target, False)
        if l < n and nums[l] == target:
            r = self.binarySearch(nums,target, True)
            return [l, r-1]
        else:
            return [-1, -1]


    def binarySearch(self, nums, target, bigger):
        n = len(nums)
        l, r = 0, n
        while l < r:
            mid = (l+r) / 2
            if nums[mid] > target:
                r = mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                if bigger:
                    l = mid + 1
                else:
                    r = mid

        return l
