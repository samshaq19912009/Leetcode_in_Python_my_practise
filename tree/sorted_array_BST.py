# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        n = len(nums)

        L, R = 0, n-1
        return self.dfs(nums, L, R)

    def dfs(self, nums, L, R):
        if L == R:
            return TreeNode(nums[L])
        if L > R:
            return None

        mid = (L+R)>> 1

        root = TreeNode(nums[mid])

        root.left, root.right = self.dfs(nums, L, mid-1), self.dfs(nums, mid+1, R)

        return root
