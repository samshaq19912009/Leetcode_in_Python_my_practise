
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        ans = []
        self.dfs(root, ans)

        return ans

    def dfs(self, node, ans):
        if node == None:
            return

        self.dfs(node.left, ans)
        ans.append(node.val)
        self.dfs(node.right, ans)


        class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        q = []

        node = root

        while node or q:
            if node:
                q.append(node)
                node = node.left
            else:
                node = q.pop()
                ans.append(node.val)
                node = node.right

        return ans
