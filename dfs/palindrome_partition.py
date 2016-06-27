class Solution:
    def partition(self, s):
        ans = []
        n = len(s)
        self.dfs([],0, n, ans,s)
        return ans

    def dfs(self, cur, start, end, ans,s):
        if start >= end:
            ans.append(cur)
            return 
        for i in range(start, end):
            tmp = s[start:i+1]
            if self.isP(tmp):
                self.dfs(cur+[tmp], i+1, end, ans, s)

        
    def isP(self, str):
        return str == str[::-1]
