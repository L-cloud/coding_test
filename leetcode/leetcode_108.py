class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def dfs(num):
            if not num:
                return
            root_index = int(len(num) / 2)
            root = TreeNode(val = num[root_index])
            root.left = dfs(num[:root_index])
            root.right = dfs(num[root_index+1:])
            return root
        return dfs(nums)
