import sys
input = sys.stdin.readline
N,M=map(int,input().split())
robot,ans = list(map(int,input().split()))+[0],0
matrix = [list(map(int,input().split())) for _ in range(N)]
xy = [[-1,0],[0,1],[1,0],[0,-1]]
while True:
    x,y,robot[2] = robot[0],robot[1],(robot[2] -1) % 4
    d = robot[2]
    matrix[x][y] = 2
    if 0<=x+xy[d][0]<N and 0<=y+xy[d][1] <M and not matrix[x+xy[d][0]][y+xy[d][1]]:
        robot[0],robot[1],robot[3] = x+xy[d][0], y+xy[d][1],0
    elif robot[3] == 3:
        if 0<= x - xy[d][0] < N and 0<= y - xy[d][1]<M and matrix[x-xy[d][0]][y-xy[d][1]] != 1:
            robot[0],robot[1],robot[3] = x-xy[d][0], y-xy[d][1],0
        else:
            break
    else:
        robot[3] += 1
print(sum(matrix[i].count(2) for i in range(N)))

