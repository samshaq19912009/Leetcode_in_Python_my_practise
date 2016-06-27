class Solution:

    def searchInsert(self, nums, target):
        #注意是要插入的位置，那必须判断当start==end的时候应该插入在哪里！！！！
        n = len(nums)
        start, end = 0, n-1

        while(start <= end):
            mid = (start+end)/2

            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                return mid

        return start 
