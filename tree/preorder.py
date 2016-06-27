class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        ans, stack = [], []


        stack.append(root)

        while stack :
            cur = stack.pop()

            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
            ans.append(cur.val)

        return ans

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        ans=[]
        self.dfs(root,ans)
        return ans

    def dfs(self,root,ans):
        if not root: return
        ans.append(root.val)
        self.dfs(root.left,ans)
        self.dfs(root.right,ans)
