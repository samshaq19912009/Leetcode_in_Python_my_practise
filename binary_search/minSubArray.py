class Solution:
    def minSubArrayLen(self, s, nums):
        size = len(nums)
        if size == 0:
            return 0
        best = size + 1
        start = 0
        end = 0
        total = 0
        while end < size:
            while end < size and total < s:
                total += nums[end]
                end += 1
            while start < end and total >= s:
                total -= nums[start]
                best = min(best, end - start)
                start += 1
    
        if best == size + 1:
            return 0
        else:
            return best

   def minSubArrayLen(self, s, nums):
       n = len(nums)
       if n == 0:
           return 0
       sums = [0 for i in range(n+1)]
       result = sys.maxint
       sums[1] = nums[0]
       for i in range(1, n+1):
           sums[i] = sum[i-1] + nums[i-1]

       for i in range(n):
           rightEnd = self.searchRight(i, n, sums[i]+s, sums)

           if rightEnd != n + 1:
               cur = rightEnd - 1
               if cur < result:
                   result = cur

       if result == sys.maxint:
           return 0
       else:
           return result


   def searchRgith(self, start, end, target, sums):
       while start+ 1 < end:
           mid = start + (end-start) / 2
           if sums[mid] >= target:
               end = mid
           else:
               start = mid
       if sums[target] >= target:
           return start
       if sums[end] >= target:
           return end
       return len(sums) + 1
