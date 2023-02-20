from typing import List
def solution(n:int, s:int) -> List[int]:
    answer = []
    while n:
        t = s // n
        if not t:
            return [-1]
        answer.append(t)
        s -= t
        n -= 1
    return sorted(answer)
