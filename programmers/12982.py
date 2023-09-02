from typing import List
def solution(d:List[int], budget:int) -> int: 
    answer = 0
    d.sort(reverse = True)
    while len(d) > 0 and budget >= d[-1]:
        budget -= d[-1]
        d.pop()
        answer += 1
    return answer
