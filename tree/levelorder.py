class Solution:
    def levelorder(self, root):
        if not root:
            return []
        result = []
        q = [root]
        while q:
            new_q = []
            ans.append([node.val for node in q])
            for node in q:
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            q = new_q
        return list(result)
