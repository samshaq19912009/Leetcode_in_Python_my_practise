class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        if not root:
            return True
        hl = self.height(root.left)
        hr = self.height(root.right)
        
        if abs(hr - hl) > 1:
            return False
            
        return self.isBalanced(root.left) and self.isBalanced(root.right)
            
        
        
    def height(self, node):
        if not node:
            return 0
        return max(self.height(node.left), self.height(node.right))+1
