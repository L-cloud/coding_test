from typing import List
def solution(n:int, stations:List[int], w:int) -> int:
    p, answer = 1,0
    stations.reverse()
    while True:
        while stations and stations[-1] - w <= p:
            p = max(p,stations.pop()+w+1)
        if n < p:
            break
        else:
            p += 2*w + 1
            answer += 1
    return answer
