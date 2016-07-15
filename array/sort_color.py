class Solution:
    def sort_color(self, nums):
        n = len(nums)
        red = 0
        blue = n - 1
        i = 0
        while i < blue + 1:
            if nums[i] == 0:
                nums[i], nums[red] = nums[red], nums[i]
                i += 1
                red += 1
                continue
            if nums[i] == 2:
                nums[i], nums[blue] = nums[blue], nums[i]
                blue -= 1
                continue
            i += 1
        return nums
