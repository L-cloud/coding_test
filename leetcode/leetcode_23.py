# Definition for singly-linked list.
import heapq
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        heap = []
        for l in lists:
            while l:
                heapq.heappush(l, (l.val, l))
                l = l.next
        head, prev = heapq.heappop(heap)[1], heapq.heappop(heap)[1]
        while heap:
            node = heapq.heappop(heap)[1]  # heap = (node.val, node)
            prev.next = node
            prev = prev.next
