class Solution:
    def __init__(self):
        self.minimum_difference = float('inf')

    def leaf_node(self, node, root_val, left, right):
        if not node:
            return float('inf')
        if left:
            if node.right:
                val = self.leaf_node(node.right, root_val, left, right)
            else:
                return node.val if node.val != root_val else float('inf')
            return val
        else:
            if node.left:
                val = self.leaf_node(node.left, root_val, left, right)
            else:
                return node.val if node.val != root_val else float('inf')
            return val

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if not root:
            return

        def dfs(node):
            if not node:  # min_val, max_val 업데이트 해주면서 넘기면 min 함수 하면 됨
                return
            left_max, right_min = self.leaf_node(node.left, node.val, True, False), self.leaf_node(node.right, node.val,
                                                                                                   False, True)
            left_child, right_child = node.left.val if node.left else float(
                'inf'), node.right.val if node.right else float('inf')
            self.minimum_difference = min(abs(node.val - left_child), abs(node.val - right_child),
                                          abs(node.val - left_max), abs(node.val - right_min), self.minimum_difference)
            dfs(node.right)
            dfs(node.left)

        dfs(root)
        return self.minimum_difference