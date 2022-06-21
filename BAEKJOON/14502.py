import sys,itertools
input = sys.stdin.readline
N,M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
cases = []
for i in range(N):
    for j in range(M):
        if not matrix[i][j]:
            cases.append([i,j])
def virus(matrix):
    h,zero = [],0
    tempt = [[matrix[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 2:
                h.append([i,j])
            elif not matrix[i][j]:
                zero += 1
    dx,dy = [-1,1,0,0],[0,0,-1,1]
    while h:
        i,j = h.pop()
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]
            if 0<=x < len(matrix) and 0<= y < len(matrix[0]) and tempt[x][y] == 0:
                tempt[x][y] = 2
                h.append([x,y])
                zero -= 1
    return zero
max_num = 0
for case1,case2,case3 in itertools.combinations(cases, 3):
    matrix[case1[0]][case1[1]], matrix[case2[0]][case2[1]], matrix[case3[0]][case3[1]]= 1,1,1
    max_num = max(virus(matrix),max_num)
    matrix[case1[0]][case1[1]], matrix[case2[0]][case2[1]], matrix[case3[0]][case3[1]]= 0,0,0
print(max_num)