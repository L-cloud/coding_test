import sys
from heapq import heappush, heappop
from typing import List
input = sys.stdin.readline
def union(a:int,b:int) -> bool:
    a, b= find(a), find(b)
    if a == b:
        return False
    parents[max(a,b)] = parents[min(a,b)]
    return True
def find(a:int) -> int:
    while a != parents[a]:
        a = parents[a]
    return a
def make_q(x:List[int]) -> None: # for memory saving, use pop()
    prev = x.pop()
    while x:
        node = x.pop()
        heappush(h,(abs(node[1] - prev[1]),prev[0],node[0]))
        prev = node
    return
N = int(input())
parents =[i for i in range(N)]
x,y,z,h = [],[],[],[]
for i in range(N):
    a,b,c = map(int,input().split())
    x.append([i,a])
    y.append([i,b])
    z.append([i,c])
func = lambda x: x[1]
x.sort(key = func); y.sort(key = func); z.sort(key = func)
make_q(x);make_q(y);make_q(z)
cnt,total = 0,0
while cnt < N -1:
    value,node1,node2 = heappop(h)
    if union(node1,node2):
        cnt += 1
        total += value
print(total)

