from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        output = ListNode()
        head = output
        while l1 and l2:
            if l1.val <= l2.val:
                output.next = ListNode(val=l1.val)
                output, l1 = output.next, l1.next
            else:  # l1 > l2
                output.next = ListNode(val=l2.val)
                output, l2 = output.next, l2.next
            print("l1 = ", l1, "l2 = ", l2, head)
        while l1:
            output.next = ListNode(val=l1.val)
            output, l1 = output.next, l1.next
        while l2:
            output.next = ListNode(val=l2.val)
            output, l2 = output.next, l2.next

        return head.next
