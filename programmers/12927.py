import heapq
from typing import List
def solution(n : int, works : List[int]) -> int:
    works = [-i for i in works]
    heapq.heapify(works)
    while n and works:
        if 1 <len(works) :
            a, b = -heapq.heappop(works), -heapq.heappop(works)
            if a - b < n :
                n -= a -b +1
                a = b - 1
            elif n < a - b:
                a -= n
                n = 0
            else:
                a -= 1
                n -= 1
            if a:
                heapq.heappush(works, -a)
            heapq.heappush(works, -b)
        else :
            return 0 if works[0] - n <= 0 else (works[0] - n) ** 2
                    
    return sum(i**2 for i in works)
