class Solution:
    def subsetII(self, nums):
        ##nums might contain duplicate
        ##!!!!
        nums.sort()
        ans = []
        self.dfs(0, [], ans, nums)
        return ans

    def dfs(self, start, path, ans, nums):
        if path[:] not in ans:
            ans.append(path)
        
        for i in range(start, len(nums)):
            path.append(nums[i])
            self.dfs(i+1, path, ans, nums)
            path.pop()
