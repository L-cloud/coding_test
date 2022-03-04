import sys

seen = {}
abc = "abcdefghijklmnopqrstuvwxyz"
alpha = sys.stdin.readline().strip()

for i, v in enumerate(alpha):
    if v in seen:
        continue
    seen[v] = i

for a in abc:
    if a in seen:
        print(seen[a], end = " ")
    else:
        print(-1, end= " ")
