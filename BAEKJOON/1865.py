import sys
input = sys.stdin.readline

T = int(input())
while T:
    T -= 1
    N, M, W = map(int, input().split())
    roads = [[float('inf') for _ in range(N + 1)] for _ in range(N + 1)]
    for _ in range(M):
        s,e,t = map(int,input().split())
        roads[s][e] = roads[e][s] = min(roads[s][e],t)
    for _ in range(W):
        s,e,t = map(int, input().split())
        roads[s][e] = -t

    for i in range(1, N + 1):
        for start in range(1,N +1):
            for end in range(1, N + 1):
                roads[start][end] = min(roads[start][end], roads[start][i] + roads[i][end])
    possible = False
    for i in range(N + 1):
        if roads[i][i] < 0:
            possible = True
            break
    if possible:
        print('YES')
        continue
    print('NO')
    