class Solution:
    def countPrime(self, n):
        ##find all the prime number less than n
        if n <= 2:
            return 0
        dp = [True] * n
        dp[0] = False
        dp[1] = False
        for i in range(2, int(math.sqrt(n))+1):
            if dp[i]:
                for j in range(i*i, n, i):
                    dp[j] = False
        
        cnt = filter(lambda x: x, dp)

        return len(cnt)

