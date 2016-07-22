class Solution:
    def reverseBit(self, n):

        ans = 0
        cnt = 0
        while n:
            ans = (ans << 1) + (n & 1)
            n = n >> 1
            cnt += 1

        ans = ans << (32-cnt)

        return ans
