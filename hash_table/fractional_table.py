class Solution:
    def fractionToDecimal(self, numerator, denominator):
        n = numerator
        d = denominator
        if n == 0:
            return "0"
        
        
        res = ''
        if n*d < 0:
            res += '-'
        n = abs(n)
        d = abs(d)
        
        if n%d == 0:
            res += str(n//d)
            return res     
        res += str(n//d) + '.'
        n %= d
        
        i = len(res)
        table = {}

        while n != 0:
            if n not in table:
                table[n] = i
            else:
                i = table[n]
                res = res[:i] + '(' + res[i:] + ')'
                return res
            n *= 10
            res += str(n // d)
            n %= d
            i += 1
        return res
