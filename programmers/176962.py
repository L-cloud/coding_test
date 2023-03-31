from typing import List
from collections import deque
def solution(plans: List[str]) ->List[str]:
    plans = deque(sorted([[name,t_i(s),t_i(p)] for name, s,p in plans], key = lambda x : x[1]))
    current = plans.popleft()
    remain_works = deque()
    answer = []

    while plans:
        if current[1] + current[2] <= plans[0][1] : 
            r_t = plans[0][1] - (current[1] + current[2])
            answer.append(current[0])
            while r_t and remain_works:
                if remain_works[0][2] <= r_t:
                    r_t -= remain_works[0][2]
                    answer.append(remain_works[0][0])
                    remain_works.popleft()
                else:
                    if remain_works:
                        remain_works[0][2] -= r_t
                    break
        else:
            current[2] -= (plans[0][1] - current[1])
            remain_works.appendleft(current)
        current = plans.popleft()    
    return answer + [current[0]] +list(n for n,v,w in remain_works)

def t_i(t:str) -> int:
    if ":" in t:
        h,m = t.split(":")
        return int(h) *60 + int(m)
    return int(t)
