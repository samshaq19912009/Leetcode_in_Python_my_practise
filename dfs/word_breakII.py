class Solution:
    def wordBreakII(self, s, wordDict):
        n = len(s)
        dp = [[False for i in range(n)] for i in range(n)]
        for i in xrange(n-1):
            for j in xrange(n-i):
                if s[i:i+j+1] in wordDict:
                    dp[i][i+j] = True

        for i in range(n):
            if dp[i][n-1]:
                ans = []
                self.dfs(0,n,[],dp,ans)
                return ans

        return []
    
    def dfs(self, cur, n, path, s, dp, ans):
        if cur == n:
            ans.append("".join(path))
            return

        for i in xrange(n):
            if dp[cur][i]:
                if path:
                    self.dfs(i+1, n, path + [' '] + [s[cur:i+1]], s, dp, ans)
                else:
                    self.dfs(i+1, n, path + [s[cur:i+1]], s, dp, ans)
                    
                    
