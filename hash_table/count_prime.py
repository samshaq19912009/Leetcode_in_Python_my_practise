class Solution:
    def count_prime(self, n):
        if n <= 2:
            return 0
        dp = [True] * n
        dp[0] = False
        dp[1] = False

        for i in range(2,int(math.sqrt(n))):
            if dp[i]:
                for j in range(i*i, n, i):
                    dp[i] = False

        cnt = filter(lambda x: x, dp)
        return len(cnt)
