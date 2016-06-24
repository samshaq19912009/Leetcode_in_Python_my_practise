class Solution:
    def subset(self, nums):
        ans = []
        n = len(nums)

        self.dfs(0,n,nums,[], ans)

        return ans

    def dfs(self, start, n, nums, path, ans):
        ans.append(path[:])

        for i in range(start,n):
            path.append(nums[i])
            self.dfs(i+1, n, nums, path, ans)
            path.pop()

        
