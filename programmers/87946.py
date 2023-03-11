from typing import List
def solution(k:int, dungeons:List[List[int]]) -> int:
    answer = 0
    def dfs(v:set, d:List[List[int]], fatigue:int ,cnt:int):
        nonlocal answer
        answer = max(answer, cnt)
        for i in list(v):
            if d[i][0] <= fatigue:
                v.remove(i)
                dfs(v, d, fatigue - d[i][1], cnt + 1)
                v.add(i)
    dfs(set(i for i in range(len(dungeons))), dungeons, k, 0)                
    return answer
