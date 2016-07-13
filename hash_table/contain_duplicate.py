"""
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numDict = {}
        n = len(nums)
        if n == 0:
            return False
        for num in nums:
            if num in numDict:
                return True
            numDict[num] = 1
        return False

