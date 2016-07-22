class Solution:
    def bitSwaprequired(self, a, b):
        x = a ^ b
        num = 0
        n = 32
        while n > 0:
            if x & 1 > 0:
                num += 1
            x = x >> 1
            n -= 1
        return num
