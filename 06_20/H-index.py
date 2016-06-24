class Solution:
    def H_index(self, citations):
        n = len(citations)
        if n < 1:
            return 0
        citations.sort(reverse=True)
        
        for i in range(n):
            if i >= citations[i]:
                return i
        
        return n
