class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        m2, m3, m5 = 0, 0, 0
        result = [1]
        for i in range(0,n-1):
            t2 = result[m2]*2
            t3 = result[m3]*3
            t5 = result[m5]*5
            
            temp = min(t2, min(t3, t5))
            
            result.append(temp)
            
            if temp == t2:
                m2 += 1
            if temp == t3:
                m3 += 1
            if temp == t5:
                m5 += 1
        
        return result[-1]
