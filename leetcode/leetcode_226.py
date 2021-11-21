class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def reverse(node):
            if not node:
                return
            node.left, node.right = node.right, node.left
            reverse(node.left)
            reverse(node.right)
        reverse(root)
        return root
