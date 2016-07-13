"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

Pay attention to overflow!!!!!!

"""
class Solution:
    def reverse_int(self, x):
        if x > 0:
            flag = 1
        else:
            flag = -1
        x = abs(x)
        ans = 0
        while x > 0:
            ans = 10*ans + x%10
            x = x / 10
        if ans > 2147483647:
            return 0
        else:
            return ans*flag
    
