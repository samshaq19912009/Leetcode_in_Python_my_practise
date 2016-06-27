class Solution:
    def pathSum(self, root, sum):
        cur = 0
        return self.dfs(root, cur, sum)

    def dfs(self, node, cur, sum):
        if not node:
            return False
        if not node.left and node.right:
            return cur+node.val == sum
        
        return self.dfs(node.left, cur+node.val, sum) or self.dfs(node.right, cur+node.val, sum)

