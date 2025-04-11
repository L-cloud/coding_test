from typing import List
def solution(s:str) -> List[int]:
    seen = {}
    answer = [0] * len(s)
    for i,v in enumerate(s):
        position = seen.get(v,-1)
        answer[i] = i - position if position != -1 else -1
        seen[v] = i
    return answer
