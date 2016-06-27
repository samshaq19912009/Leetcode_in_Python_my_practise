class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        Solution.res = []
        self.dfs(s, wordDict, '')
        return Solution.res
        
    def check(self, s, wordDict):
        n = len(s)
        f = [False for i in range(n+1)]
        f[0] = True
        for i in range(1, n+1):
            for j in range(0,i):
                if f[j] and s[j:i] in wordDict:
                    f[i] = True
                        
        return f[n]
            
    def dfs(self, s, wordDict, stringlist):
        if self.check(s, wordDict):
            if len(s) == 0:
                Solution.res.append(stringlist[1:])
            for i in range(1, len(s)+1):
                if s[:i] in wordDict:
                    self.dfs(s[i:], wordDict, stringlist+' '+s[:i])
