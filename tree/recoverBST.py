

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.pre, self.first, self.second = None, None, None
        self.dfs(root)
        self.first.val, self.second.val = self.second.val, self.first.val
        
        
    def dfs(self, root):
        if not root:
            return 
        self.dfs(root.left)
        
        if self.pre and self.pre.val > root.val:
            if not self.first:
                self.first = self.pre
            self.second = root

              
              
        self.pre = root
        self.dfs(root.right)
