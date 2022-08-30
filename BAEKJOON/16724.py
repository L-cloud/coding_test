import sys
input = sys.stdin.readline
N,M = map(int,input().split())
matrix = [list(input().strip()) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
cmd,ans = {'D':(1,0),'U' : (-1,0), 'L' : (0,-1), 'R' : (0,1)},0
def check(i:int, j:int) -> int:
    tempt = set()
    while not visited[i][j]:
        visited[i][j] = True
        tempt.add((i,j))
        i ,j= i + cmd[matrix[i][j]][0], j + cmd[matrix[i][j]][1] # 변수 최소화
        if (i,j) in tempt:
            visited[i][j] = True
            return 1
    return 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            ans += check(i,j)
print(ans)

