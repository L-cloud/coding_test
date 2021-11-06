class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        one_to_n = [i for i in range(1,n + 1)]
        output,tempt =[],[]
        def dfs(candi : List):
            if len(tempt) == k :
                output.append(tempt[:])
                return
            for index, value in enumerate(candi):
                next_list = candi[index+1 :]
                tempt.append(value)
                dfs(next_list)
                tempt.pop()
        dfs(one_to_n)
        return output
