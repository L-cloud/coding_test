# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_lenght : int = 0
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node, value):
            if not node:
                return None, 0 # val, lenght
        
            left_val, left_lenght = dfs(node.left, node.val)
            right_val, right_lenght = dfs(node.right, node.val)
            lenght = max(left_lenght, right_lenght)
            
            if left_val != None and left_val == right_val: ### not left_val x because of 0 !!!!!!
                self.max_lenght = max(self.max_lenght, left_lenght + right_lenght)
            else:
                 self.max_lenght = max(self.max_lenght, lenght)
            
            if node.val == value:
                lenght += 1
            else: 
                lenght = 0
            return node.val, lenght
        
        if root:   
            dfs(root, root.val)
        
        return self.max_lenght
                
