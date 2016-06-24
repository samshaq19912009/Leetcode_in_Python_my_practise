class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [ 100000] * (n+1)
        
        dp[1] = 1
        for i in range(1, n+1):
            j = 1
            while j*j <= i:
                if j*j == i:
                    dp[i] = 1
                    break
                dp[i] = min(dp[i], dp[i-j*j]+1)
                j += 1
                
        return dp[n]


class Solution(object):
    _dp = [0]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = self._dp
        while len(dp) <= n:
                dp += min(dp[-i*i] for i in range(1,int(len(dp)**0.5+1))) + 1,
        return dp[n]        

