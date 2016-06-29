class Solution:
    def combinationSum(self, candidates, target):
        path = []
        ans = []
        candidates.sort()

        self.dfs(0, target, candidates, path, ans)

        return ans
    

    def dfs(self, start, left, candidates, path, ans):
        
        if left == 0:
            candidates.append(path[:])
            return

        for i in range(start, len(candidates)):
            if candidates[i] > left:
                continue
            path.append(candidates[i])
            self.dfs(i, left-candidates[i], candidates,  path, ans)
            path.pop()

