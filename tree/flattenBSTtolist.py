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
        ##connect the right tree after the left tree
        p.right = root.right
        #now the left tree is the right of the node
        root.right = root.left
        #the left should be none
        root.left = None
        
