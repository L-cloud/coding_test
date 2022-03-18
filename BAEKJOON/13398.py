import sys


m,n = map(int, sys.stdin.readline().split()) #col, row
stack = [[i,j] for j in range(m) for i in range(n)]
tomato = []
for _ in range(n):
    tomato.append(list(map(int, sys.stdin.readline().split())))
while stack:
    row, col = stack.pop()
    if tomato[row][col] == 1: # 중복 처리문제 어떻게 해결할지 고민 ㄱ
        if row > 0:
            stack.append([row-1,col])
        if col < m - 1:
            stack.append([row, col + 1])
        if row < n - 1:
            stack.append([row+1,col])
        if col > 0:
            stack.append([row,col -1])
