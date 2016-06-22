class Solution:
    def kthBST(self, root, k):
        if not root:
            return None
        ans = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            ans.append(node.val)
            if len(ans) == k:
                return ans[-1]
            dfs(node.right)

        dfs(root)
        return ans[-1]


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        node = root
        while node:
            stack.append(node)
            node = node.left
        x = 0
        while stack and x < k:
            node = stack.pop()
            x += 1
            right = node.right
            while right:
                stack.append(right)
                right = right.left
        return node.val
