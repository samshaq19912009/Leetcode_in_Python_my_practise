class Solution:
    def uniqueBST(self, n):

        ans = [0] * (n+1)

        ans[0] = 1

        ans[1] = 1

        for i in range(2, n+1):
            for j in range(0, i):
                ans[i] += ans[j] * ans[i-1-j]

        return ans[n]
