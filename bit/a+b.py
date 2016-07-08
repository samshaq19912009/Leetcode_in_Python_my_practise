class Solution:
    ##TLE error
    def add(self, a, b):
        #add a and b
        #do not use arithemstic operator
        while b != 0:
            a = a ^ b
            carry = a & b
            b = carry << 1
        
        return a
        
