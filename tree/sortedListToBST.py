class Solution:
    def sortedListToBST(self, head):
        if not head:
            return None
        tail, length = head, 0
        while tail:
            length += 1
            tail = tail.next
        return self.dfs(head, 0, length-1)
    
    def dfs(self, head, L, R):
        if L == R:
            return TreeNode(head.val)
        if L > R:
            return None
        cnt = 0
        mid = (L+R)>>1
        tmp = head
        while cnt < mid:
            cnt += 1
            tmp = tmp.next
        root = TreeNode(tmp.val)
        root.left, root.right = self.dfs(head, L, mid-1), self.dfs(tmp.next, mid+1, R)
        return root
