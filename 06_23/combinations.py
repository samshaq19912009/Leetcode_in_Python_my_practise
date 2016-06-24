class Solution:
    #Given n and k, return all possible combinations of k numbers
    #within n
    def combinations(self, n, k):
        if k == 1:
            return [i+1 for i in range(n)]

        if n > k:
            return [[n] + r for r in self.combine(n-1,k-1)] + self.combine(n-1,k)
        else:
            return [[n] + r for r in self.combine(n-1,k-1)]
        
        
           

