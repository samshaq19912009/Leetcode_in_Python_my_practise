class Solution:
    def findItineray(self, tickets):

        n, self.ans = len(tickets) + 1, ['JFK']
        m = collections.defaultdict(lambda : collections.OrderedDict())
        for x , y in sorted(tickets):
            m[x].setdefault(y, 0)
            m[x][y] += 1

        self.dfs(['JFK'], n, m)

        return ans


    def dfs(self, cur, n, m):
        if len(ans) == n:
            return True

        if cur in m:
            for y, cnt in m[cur].items():
                if cnt > 0:
                    m[cur][y] -=1
                    self.ans += [y]
                    if self.dfs(y, n, m):
                        return True
                    m[cur][y] += 1
                    self.ans = self.ans[:-1]

        return False 
