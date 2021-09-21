# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object): # bad performance version
    def insertionSortList(self, head):
        def dfs(head, next_node,index):
            if not next_node:
                return
            node = head
            try_num = 0
            while try_num < index:
                if node.val > next_node.val:
                    next_node.val, node.val = node.val,next_node.val
                try_num += 1
                node = node.next
            dfs(head, next_node.next, index + 1)
        
        dfs(head, head.next,1)
        return head
