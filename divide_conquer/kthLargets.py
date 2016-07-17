"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

"""

class Solution:
    def findKth(self, nums, k):
        import random
        pivot = random.choice(nums)
        num1, num2 = [], []
        for num in nums:
            if num > pivot:
                num1.append(num)
            elif num < pivot:
                num2.append(num)
        if k <= len(num1):
            return self.findKth(num1, k)
        elif k > len(num) - len(num2):
            return self.findKth(num2, (k - len(num) - len(num2)))
        return pivot

    def heap_solution(self, nums, k):
        heap = []
        res = []
        for i in nums:
            heapq.heappush(heap, -i)
        for j in range(k):
            res = -heapq.heappop(heap)
        
        return res
