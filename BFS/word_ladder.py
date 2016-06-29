class Solution:
    def wordLadder(self, start, end, dic):
        if start == end:
            return 1
        n = len(start)
        
        atoz = map(chr, xrange(ord('a'), ord('z')+1))

        q, vis, dis = [start], set(), 2
        vis.add(start)
        while q:
            for i in xrange(len(q)):
                cur = q.pop(0)
                for j in xrange(n):
                    for k in atoz:
                        t = cur[:j] + k + cur[j+1:]
                        if t == end:
                            return dis
                        if t in dic and t not in vis:
                            q.append(t)
                            vis.add(t)
            dis += 1
            
        return 0
