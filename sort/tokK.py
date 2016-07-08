class Solution(object):
    def topKFrequent(self, nums, k):
        n = len(nums)
        cntDict = collections.defaultdict(int)
        
        for i in nums:
            cntDict[i] += 1
        freqlist = [ [] for i in range(n+1)]

        for p in cntDict:
            freqlist[cntDict[p]] += p,
        ans = []
        for p in range(n, 0, -1):
            ans += freqlist[p]

        return ans[:k]

