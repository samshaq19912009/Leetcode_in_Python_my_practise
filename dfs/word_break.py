class Solution:
    def wordBreak(self, s, wordDict):
        n = len(s)
        f = [False for i in range(n+1)]
        f[0] = True
        for i in range(n+1):
            for j in range(i):
                if f[j] and s[j:i] in wordDict:
                    f[i] = True


        return f[n]
