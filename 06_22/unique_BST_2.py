class Solution:
    def generateBST(self, n):

        return self.dfs(1,n)



    def dfs(self, s, e):

        if s > e:
            return [None]

        ans = []
        for i in range(s, e+1):
            L = self.dfs(s, i-1)
            R = self.dfs(i+1, e)

            for left in L:
                for right in R:
                    root = TreeNode(i)
                    root.left, root.right = left, right
                    ans.append([root])

        return ans
