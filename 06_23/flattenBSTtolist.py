class Solution:
    def flatten(self, root):
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left == None:
            return
        p = root.left
        ##find the end of the left tree
        while p.right:
            p = p.right
        p.right = root.right
        root.right = root.left
        root.left = None
        
