import sys,itertools

N,M = map(int,(sys.stdin.readline().split()))
chicken = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
c,h, answer = [],[], float('inf')
for i in range(N):
    for j in range(N):
        if chicken[i][j] == 1:
            h.append([i,j])
        elif chicken[i][j] == 2:
            c.append([i,j])
for candi in itertools.combinations(c,M):
    tempt1 = 0
    for house in h:
        tempt2 = float('inf')
        for c in candi:
            tempt2 = min(abs(house[0] - c[0]) + abs(house[1] - c[1]), tempt2)
        tempt1 += tempt2 # 가장 가까운 녀석 더하기
    answer = min(answer, tempt1)
print(answer)
    
    