import sys
from heapq import heappush, heappop
from typing import List
input = sys.stdin.readline
N = int(input())
def check(q:List) -> None:
    while q and not p[q[0][1]]:
        heappop(q)
    if q:
        p[q[0][1]] = False
    return q[0][0] if q else None
for _ in range(N):
    T,cnt = int(input()),0
    min_q,max_q,p = [],[],[True for _ in range(T)]
    for i in range(T):
        cmd = input().split()
        if cmd[0] == 'D':
            if cmd[1] == '-1':
                check(min_q)
            else:
                check(max_q)
        else:
            heappush(min_q,(int(cmd[1]),i))
            heappush(max_q,(-int(cmd[1]),i))
    ma,mi = check(max_q),check(min_q)
    if ma == None and mi == None:
        print("EMPTY")
    elif mi == None:
        print(-ma, -ma)
    else:
        print(-ma, mi)
    
