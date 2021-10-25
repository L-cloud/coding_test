# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next or left == right:
            return head
        root, right = ListNode(), right - left
        output,root.next = root,head
        while left > 1 :
            root = root.next
            left -= 1
        link_node,start_node, next_node = root.next,root.next, root.next.next
        while right > 0 :
            tempt, next_node.next, next_node = next_node,start_node, next_node.next
            start_node = tempt
            right -= 1
        root.next,link_node.next = start_node,next_node
            
        return output.next
