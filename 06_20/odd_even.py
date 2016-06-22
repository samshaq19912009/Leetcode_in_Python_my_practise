class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        p, q = head, head

        while q:
            q = q.next
            if not q or not q.next:
                break
            next_p = p.next
            next_q = q.next
            q.next = next_q.next
            p.next = next_q
            next_q.next = next_p
            p = p.next

        return head
