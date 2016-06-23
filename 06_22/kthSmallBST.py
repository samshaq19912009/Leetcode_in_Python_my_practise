class Solution:
    def kthSmallestBST(self, root, k):
        ##recursive
        ans = []
        def dfs(node):
            if not node:
                return []
            dfs(node.left)
            ans.append(node.val)
            if len(ans) == k:
                return
            dfs(node.right)
            
        dfs(root)
        return ans[-1]

    def kthSmallest(self, root, k):
        ##iterative
        stack = []
        node = root
        while node:
            stack.append(node)
            node = node.left
        
        x = 0
        while x < k and stack:
            node = stack.pop()
            x += 1
            right = node.right
            while right:
                stack.append(right)
                right = right.left

        return node.val
