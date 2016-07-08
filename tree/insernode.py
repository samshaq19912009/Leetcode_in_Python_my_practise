class Solution:
    def insertNode(self, root, node):
        #insert a node into a binary search tree
        if root == None:
            root = node
            return node

        self.helper(root, node)

        return root

    def helper(self, root, node):
        cur = root

        if root.val <= node.val:
            if root.right == None:
                root.right = node
                return
            else:
                self.helper(root.right, node)
        
        else:
            if root.left == None:
                root.left = node
                return
            else:
                self.helper(root.left, node)
