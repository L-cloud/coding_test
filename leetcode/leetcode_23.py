# Definition for singly-linked list.
import heapq
from typing import Optional, List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap, ecount = [], 0
        for l in lists:
            while l:
                heapq.heappush(heap, (l.val, ecount, l))  # priority, ecount, task
                l = l.next
                ecount += 1
        if heap == []:
            return
        prev = heapq.heappop(heap)[2]
        head = prev
        prev.next = None
        while heap != []:
            node = heapq.heappop(heap)[2]  # heap = (node.val, ecount ,node)
            node.next = None
            prev.next = node
            prev = prev.next
        return head

