class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = collections.Counter(nums)
        heap = []

        for key,value in counts.items():
            if len(heap) < k:
                heapq.heappush(heap,(value,key))

            else:
                if heap[0][0] < value:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (value, key))

        return [x[1] for x in heap]
