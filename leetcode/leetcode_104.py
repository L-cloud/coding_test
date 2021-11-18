class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        m_depth = [1]
        def dfs(node, depth):
            if not node:
                return
            m_depth[0] = max(m_depth[0], depth)
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        dfs(root, 1)
        
        return m_depth[0]

