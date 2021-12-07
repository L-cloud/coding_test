class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return
        val = preorder.pop(0)
        root = TreeNode(val = val)
        root.left = self.buildTree(preorder, inorder[:inorder.index(val)])
        root.right = self.buildTree(preorder, inorder[inorder.index(val) + 1:])
        return root
