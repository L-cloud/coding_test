class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(node : TreeNode, add_ : int):
            if not node:
                return add_
            right_val = dfs(node.right, add_)
            node.val += right_val
            left_val = dfs(node.left, node.val)
            return max(node.val, left_val)
        dfs(root,0)
        return root    
