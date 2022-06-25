
import sys
def circle():
    prev1, prev2 = 0, 0
    r1,r2 = air[0][0], air[1][0]
    for i in range(1, len(matrix[0])):
        next_1, next_2 = matrix[r1][i], matrix[r2][i]
        matrix[r1][i], matrix[r2][i] = prev1, prev2
        prev1, prev2 = next_1, next_2
    up(prev1, 1)
    down(prev2, 2)
def left(prev,direction):
    if direction == 1:
        for i in range(len(matrix[0]) - 2, -1, -1):
            next_ = matrix[0][i]
            matrix[0][i] = prev
            prev = next_ 
        down(prev, direction)
    else:
        for i in range(len(matrix[0]) -2,-1,-1):
            next_ = matrix[-1][i]
            matrix[-1][i] = prev
            prev = next_  
        up(prev, direction)
def up(prev, direction):
    if direction == 1:
        for i in range(air[0][0] -1, -1, - 1):
            next_ = matrix[i][-1]
            matrix[i][-1] = prev
            prev = next_
        left(prev,direction)
    else:
        for i in range(len(matrix) -2, air[1][0], -1):
            next_ = matrix[i][0]
            matrix[i][0] = prev
            prev = next_
        return
def down(prev, direction):
    if direction == 1:
        for i in range(1,air[0][0]):
            next_ = matrix[i][0]
            matrix[i][0] = prev
            prev = next_
        return
    else:
        for i in range(air[1][0] + 1, len(matrix)):
            next_ = matrix[i][-1]
            matrix[i][-1] = prev
            prev = next_
        left(prev,direction)
        
R,C,T = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
air = [[r,0] for r in range(R) if matrix[r][0] == -1]
dx,dy = [1,-1,0,0],[0,0,1,-1]
direction = [1,1]
while T:
    T -= 1
    plus = []
    for i in range(R):
        for j in range(C):
            if 4 < matrix[i][j] : 
                dust = matrix[i][j] // 5
                for k in range(4):
                    x = dx[k] + i
                    y = dy[k] + j
                    if 0<=x <R and 0<= y < C and matrix[x][y] != -1:
                        matrix[i][j] -= dust
                        plus.append([x,y,dust])
    while plus:
        i, j, dust = plus.pop()
        matrix[i][j] += dust
    circle()
output = [sum(matrix[i]) for i in range(R)]
print(sum(output) + 2)