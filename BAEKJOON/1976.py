import sys
input = sys.stdin.readline
N,M = int(input()),int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]
path = list(map(int,input().split()))
p = {k : set([i for i,v in enumerate(matrix.pop(),1) if v]) for k in range(N,0,-1)}
for key in p: #갈 수 있는 경로 모두 update
    tempt = set(p[key]) # 새 객채로 해줘야함
    while tempt:
        node = tempt.pop()
        for n in p[node]:
            if n not in p[key]:
                p[key].add(n)
                tempt.add(n)
for i in range(M-1):
    if path[i+1] != path[i] and path[i+1] not in p[path[i]]:
        print("NO")
        exit()
print("YES")
