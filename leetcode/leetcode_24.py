from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        slow, fast = head, head.next
        while fast:  # hmm just change value that is simple
            slow.val, fast.val = fast.val, slow.val
            slow, fast = fast.next, fast.next.next if fast.next else None
        return head
