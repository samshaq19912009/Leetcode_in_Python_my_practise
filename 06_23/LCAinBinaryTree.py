class Solution:
    def lowwestcommonAncestor(self, root, p, q):
        if not root or not p or not q:
            return root

        left = self.lowwestcommonAncestor(root.left, p, q)
        right = self.lowestcommonAncestor(root.right, p, q)

        if left and right:
            return root
        elif not left:
            return right
        else:
            return left
