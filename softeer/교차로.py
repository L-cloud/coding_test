import sys
from heapq import heappop
from collections import OrderedDict
input = sys.stdin.readline
def check(a:str) -> str:
    d = {'A':'D', 'D':'C','C':'B','B':'A'}
    return d[a]
N = int(input())
p,v = [-1] * N,{"A":0,"B":0, "C":0,"D":0}
q = [(i,tuple(input().split()))for i in range(N)]

time = int(q[0][1][0])
t = OrderedDict()
while q:
    while q and int(q[0][1][0]) <= time:
        index,node = heappop(q)
        t.update({node:index})
        v[node[1]] += 1
    while t:
        t_t, t_v = [], set()
        for k in t:
            if not v[check(k[1])] and k[1] not in t_v:
                t_t.append(k)
                t_v.add(k[1])        
        if not t_t: 
            print('\n'.join([str(i) for i in p]))
            exit()
        for k in t_t:
            p[t[k]] = time
            v[k[1]] -= 1
            del t[k]
        time += 1
        while q and int(q[0][1][0]) <= time:
            index,node = heappop(q)
            t.update({node:index})
            v[node[1]] += 1
    time = max(time,int(q[0][1][0])) if q else 0
print('\n'.join([str(i) for i in p]))
