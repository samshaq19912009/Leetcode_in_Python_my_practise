class Solution:
    def sqrt(self, x):
        r = x
        while r*r > x:
            r = int( (r + x/r) / 2)
        return r
