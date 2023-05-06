from typing import List,Dict, Tuple
from collections import defaultdict
from heapq import heappop,heappush
def solution(n:int, s:int, a:int, b:int, fares:List[List[int]]) -> int: #지점 갯수, 출발지점 s / a,b 도착지점/ 요금
    road = defaultdict(dict)
    v = dict()
    h = [(0,s,s)]
    for a1,b1,c in fares:
        road[a1][b1] = c
        road[b1][a1] = c
    v[(s,s)] = 0
    while h:
        cost, m, ap = heappop(h)
        if m != a:
            for i in road[m]: # 무지 움직임 근데 도착하면 안 움직여도 됨
                if m == ap: # 같이 움직임
                    if (i,i) not in v or  cost + road[m][i] < v[(i,i)]: 
                        heappush(h,(cost + road[m][i], i, i))
                        v[(m,i)] = cost + road[m][i]
                if (i,ap) not in v or cost + road[m][i] < v[(i,ap)]:
                    heappush(h,(cost + road[m][i],i,ap))
                    v[(i,ap)] =  cost + road[m][i]
        if ap != b :
            for i in road[ap]: # 어피치 움직임
                if (m,i) not in v or cost + road[ap][i] < v[(m,i)]:
                    heappush(h,(cost + road[ap][i],m,i))
                    v[(m,i)] = cost + road[ap][i]
        if a == m and b == ap:
            return cost
