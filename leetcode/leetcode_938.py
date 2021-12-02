class Solution:
    def __init__(self):
        self.total = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return
        if high <= root.val:
            if root.val == high:
                self.total += high
            self.rangeSumBST(root.left, low, high)
        elif  root.val <= low:
            if root.val == low:
                self.total += low
            self.rangeSumBST(root.right, low, high)
        
        else: # low < root.val < high
            self.total += root.val
            self.rangeSumBST(root.right, low, high)
            self.rangeSumBST(root.left, low, high)
        
        return self.total
