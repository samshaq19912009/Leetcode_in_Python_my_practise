class Solution:
    def isBST(self, node):
        INT_MIN = -4294967296
        INT_MAX = 4294967296
        
        return self.check(node, INT_MIN, INT_MAX)

    def check(node, min, max):
        if node is None:
            return True
        if node.data < min or node.data > max:
            return False
        
        return self.check(node.left, min, node.data-1) and self.check(node.right, node.data+1, max)
    
