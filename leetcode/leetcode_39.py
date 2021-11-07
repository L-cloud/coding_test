class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output, candi = [],[]
        def dfs(c : List[int],start:int):
            if sum(c) > target or start >= len(candidates):
                return
            if sum(c) == target:
                output.append(candi[:])
                return
            for i,v in enumerate(candidates[start:]):
                candi.append(v)
                dfs(candi,start + i)
                candi.pop()
        dfs(candi,0)
        return output
