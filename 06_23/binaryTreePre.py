class Solution:
    def preOrder(self, root):
        if not root:
            return []
        q = []
        ans = []
        
        q.append(root)
        
        while q:
            node = q.pop()
            ans.append(node.val)
            if node.right:
                ans.append(node.right)
            if node.left:
                ans.append(node.left)
        
        return ans

    #recursive
    def preOrder(self, root):
        ans = []
        if not root:
            return ans
        self.dfs(root, ans)
        
    def dfs(self, root, ans):
        if not root:
            return 
        ans.append(node.val)
        dfs(root.left, ans)
        dfs(root.right, ans)
