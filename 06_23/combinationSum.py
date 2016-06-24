class Solution:
    def combinationSum(self, candidates, target):
        ans = []
        
        self.dfs(0, target, [], ans, candidates)

        return ans

    def dfs(self, start, left, path, ans, candidates):
        if left == 0:
            ans.append(path[:])
            return

        for i in range(start, len(candidates)):
            if candidates[i] > left:
                return

            path.append(candidates[i])
            self.dfs(i, left-candidates[i], path, ans, candidates)
            path.pop()


