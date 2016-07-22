class Solution:
    def mergeKlist(self, lists):
        heap = []
        for node in lists:
            if node:
                heapq.heappush(heap,(node.val, node))
        head = ListNode(0)
        cur = head
        while heap:
            node = heappq.heappop(heap)
            cur.next = ListNode(node[0])
            if node[1].next:
                heapq.heappush(heap, (node[1].next.val, node[1].next))
        return head.next
