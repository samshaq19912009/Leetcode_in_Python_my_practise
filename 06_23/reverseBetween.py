class Solution:
    def reverseBetween(self, head, m, n):
        if not head or head.next == None:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        head1 = dummy

        for i in range(m-1):
            head1 = head1.next

        p = head1.next
        
        for j in range(n-m):
            tmp = p.next
            p.next = p.next.next
            tmp.next = head1.next
            
            head1.next = tmp

        return dummy.next
