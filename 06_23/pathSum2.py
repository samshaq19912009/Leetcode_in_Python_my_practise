class Solution:
    def pathSum(self, root, sum):
        ans = []
        path = []
        cur = 0
        self.dfs(root, cur, sum, path, ans)

        return ans

    def dfs(self, node, cur, sum, path, ans):
        if not node:
            return

        if not node.left and not node.right:
            if node.val+cur == sum:
                path.append(node.val)
                ans.append(path[:])
                ans.pop()
        path.append(node.val)
        self.dfs(node.left, cur+node.val, sum, path, ans)
        self.dfs(node.right, cur+node.val, sum, path , ans)

