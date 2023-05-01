import heapq
from typing import List
def solution(A:List[int],B:List[int]) -> int:
    B = [-i for i in B]
    heapq.heapify(A)
    heapq.heapify(B)
    answer = 0
    while A:
        answer += (heapq.heappop(A) * (-heapq.heappop(B)))
    return answer
