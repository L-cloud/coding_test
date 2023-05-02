from heapq import heappop, heappush, heapify
from typing import List
def solution(N:int, road:List[List[int]], K:int) -> int:
    costs = [[float('inf') for _ in range(N)] for _ in range(N)]
    for a,b,c in road:
        costs[a-1][b-1] = min(costs[a-1][b-1], c)
        costs[b-1][a-1] = min(costs[b-1][a-1],c)
    h = [(-v,i) for i,v in enumerate(costs[0]) if v != float('inf')]
    heapify(h)
    while h:
        v = heappop(h)
        v, i = -v[0], v[1]
        for index,value in enumerate(costs[i]):
            if v + value < costs[0][index] and v + value <= K :
                costs[0][index] = v + value
                heappush(h,(-(costs[0][index]),index))

    return sum([1 for i in costs[0] if i <= K]) + (costs[0][0] == float('inf'))
