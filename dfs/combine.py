##dfs will exceed time limit!!!!
class Solution:
    def combinationSum(self, n, k):

        ans = []

        def dfs(start, sums, path):
            if len(path) == k and sums == n:
                ans.append(path)
                return

            if len(path) > k  or sums > n:
                return

            for x in range(start+1, 10):
                dfs(x, sums+x, path+[x])

        dfs(0,0,[])

        return ans
    
    def combine(self, n, k):
        if k == 1:
            return [[i+1] for i in range(n)]

        if n > k:
            return [ [n] + r for r in self.combine(n-1,k-1)] + self.combine(n-1,k)
        else:
            return [ [n] + r for r in self.combine(n-1,k-1)]
