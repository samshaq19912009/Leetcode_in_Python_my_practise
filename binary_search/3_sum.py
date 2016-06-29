class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        n = len(nums)
        ans = []
        for i in range(n-2):
            if i == 0 or nums[i] > nums[i-1]:
                left = i + 1
                right = n - 1
                while left < right:
                    if nums[left] + nums[right] == 0 - nums[i]:
                        ans.append([nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1

                    elif nums[left] + nums[right] < 0 - nums[i]:
                        while left < right:
                            left += 1
                            if nums[left] > nums[left-1]:
                                break

                    else:
                        while left < right:
                            right -= 1
                            if nums[right] < nums[right+1]:
                                break

        return ans
