# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_str,l2_str,output = "","",ListNode()
        for_output = output
        while l1: #reverse l1
            l1_str = str(l1.val) + l1_str
            l1 = l1.next
            
        while l2: # revese l2
            l2_str = str(l2.val) + l2_str
            l2 = l2.next
        
        sum_ = str(int(l1_str) + int(l2_str))
        
        for char in sum_[::-1]:
            for_output.next = ListNode(int(char))
            for_output = for_output.next
        
        return output.next
        
