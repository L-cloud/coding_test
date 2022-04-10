import sys
from functools import reduce
N = int(sys.stdin.readline())
P = list(map(int,sys.stdin.readline().split()))
P.sort()
# P = [P[i-1] + P[i] if i > 0 else P[i] for i in range(N)] # update가 안 됨
for i in range(N):
    if i < 1:
        continue
    P[i] = P[i -1] + P[i]
print(sum(P))


