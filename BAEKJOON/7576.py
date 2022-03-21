import sys
import collections
m,n = map(int, sys.stdin.readline().split()) #col, row
stack = collections.deque([[i,j] for j in range(m) for i in range(n)])
tomato, day,visited = [], 0, set()
for _ in range(n):
    tomato.append(list(map(int, sys.stdin.readline().split())))

while stack:
    for _ in range(len(stack)):
        row, col = stack.popleft()
        if tomato[row][col] == 1: # 중복 처리문제 어떻게 해결할지 고민 
            if row > 0:
                if tomato[row - 1][col] == 0 and (row - 1,col) not in visited:
                    stack.append([row-1,col])
                    visited.add((row-1, col))
            if col < m - 1:
                if tomato[row][col + 1] == 0 and (row, col + 1) not in visited:
                    stack.append([row, col + 1])
                    visited.add((row,col + 1))
            if row < n - 1:
                if tomato[row + 1][col] == 0 and (row+1, col) not in visited:
                    stack.append([row + 1, col])
                    visited.add((row+1, col))
            if col > 0:
                if tomato[row][col - 1] == 0 and (row, col-1) not in visited:
                    stack.append([row,col -1])
                    visited.add((row,col -1))
    day += 1
    for row, col in stack:
        tomato[row][col] =1

for i in range(len(tomato)):
    if 0 in tomato[i]:
        print(-1)
        exit()
print(day - 1) # 마지막에 다 채우더라도 stack에 들어가서 한 번 더 돌음 -1 해줘야함
