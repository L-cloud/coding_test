class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output, tempt = [[]], []
        def dfs(length: int,index:int):
            for i,value in enumerate(nums[index:]):
                tempt.append(value)
                if len(tempt) == length:
                    output.append(tempt[:])
                dfs(length+1, index + 1 + i)
                tempt.pop()
                
        dfs(1,0)
        return output

