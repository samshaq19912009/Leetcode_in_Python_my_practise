class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.n = len(nums)
        self.table = [0 for i in range(self.n+1)]
        self.table[0] = 0
        for i in range(1,self.n+1):
            self.table[i] += self.table[i-1] + nums[i-1]

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.table[j+1] - self.table[i]
