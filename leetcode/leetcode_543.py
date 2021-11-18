class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_lenght =[0]
        def dfs(node):
            if not node:
                return -1
            left_node = dfs(node.left)
            right_node = dfs(node.right)
            level = max(left_node, right_node) + 1
            max_lenght[0] = max(max_lenght[0], left_node+right_node +2)
            return level
        dfs(root)
        return max_lenght[0]
