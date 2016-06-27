class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L, R = 0, len(nums)-1

        while L < R:
            mid = (L+R)/2
            if nums[mid] <= nums[R]:
                R = mid
            else:
                L = mid+1

        return nums[L]
