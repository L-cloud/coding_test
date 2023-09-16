from typing import List, Deque
from collections import deque
def solution(cap:int, n:int, deliveries:List[int], pickups:List[int]) -> int:
    d_q = deque([[i,v] for i, v in enumerate(deliveries,1) if v])
    p_q = deque([[i,v] for i, v in enumerate(pickups,1) if v])
    answer = 0
    while d_q and p_q:
        max_r = max(d_q[-1][0], p_q[-1][0]) # 아... 그냥 이렇게 한 다음 다음에 하면 됨
        answer += 2*max_r
        pop(cap,d_q)
        pop(cap,p_q)
    while d_q:
        answer += 2*d_q[-1][0]
        pop(cap,d_q)
    while p_q:
        answer += 2*p_q[-1][0]
        pop(cap,p_q)
    return answer

def pop(capa:int, q:Deque[int]) -> int:
     while capa and q:
        if q and q[-1][-1] <= capa:
            capa -= q[-1][-1]
            q.pop()
            continue
        if q : q[-1][-1] -= capa
        return
