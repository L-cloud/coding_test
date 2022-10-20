from typing import List
from collections import deque
def solution(queue1:List[int], queue2:List[int]) -> int:
    cnt,answer = len(queue1) + len(queue2), 0
    q1,q2 = deque(queue1), deque(queue2)
    s_q1,s_q2 = sum(q1), sum(q2)
    while answer <= cnt + 2: ## 왜지?
        if s_q1 < s_q2:
            q1.append(q2.popleft())
            s_q2 -= q1[-1] 
            s_q1 += q1[-1]
        elif s_q2 < s_q1:
            q2.append(q1.popleft())
            s_q1 -= q2[-1]
            s_q2 += q2[-1]
        else:
            return answer
        answer += 1
    return -1
