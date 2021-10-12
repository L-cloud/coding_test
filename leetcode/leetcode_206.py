# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev = None
        while head:
            rev, rev.next, head = head, rev, head.next
        return rev
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: #using recursion
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next_, node.next = node.next, prev
            return reverse(next_, node)
        return reverse(head)
