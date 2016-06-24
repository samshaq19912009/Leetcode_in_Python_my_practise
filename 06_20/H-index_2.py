class Solution:
    def H_index(self, citations):
        #citations already sorted ascending
        #for i min(n-i, citations[i])
        n = len(citations)
        L , R = 0, n
        
        while L < R:
            mid = (L+R)>>1
            if n - mid <= citations[mid]:
                R = mid
            else:
                L = mid + 1
        
        return n - L
