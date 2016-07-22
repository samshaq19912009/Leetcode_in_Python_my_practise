class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans = []
        start = 1
        tmp = []
        self.dfs(start, tmp, ans, k, n)
        
        return ans
        
    def dfs(self, start, tmp, ans, k, left):
        if len(tmp) == k:
            if left == 0:
                ans.append(tmp[:])
            return
        
        for i in range(start, 10):
            if i > left:
                break
            tmp.append(i)
            self.dfs(i+1, tmp, ans, k, left-i)
            tmp.pop()
