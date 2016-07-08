class Solution:
    def longestCommon(self, A, B):
        l1 = len(A)
        l2 = len(B)

        if l1 == 0 or l2 == 0:
            return 0

        dp = [[0 for j in range(l2+1)] for i in range(l1+1)]

        for i in range(l1+1):
            dp[i][0] = 0
        for j in range(l2+1):
            dp[0][j] = 0

        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[l1][l2]
