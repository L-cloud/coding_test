# Dummy 도스 게임
# 벽 or 자기자신 몸과 부딪히면 게임 끝
# N*N 몇몇 칸 사과 AND  보드 상하좌우 끝에 벽
# 뱀 0,0 위치 
# 몸길이 늘려 다음칸으로 -> 사과 있으면 꼬리 그대로// 없으면 꼬리 당겨서 길이 유지


# 보드 크기 N, 사과 갯수 K, 방향 변환 횟수 L
# 정수 X, 문자 C -> X초 뒤에 왼쪽 or 오른쪽으로 90도 회전 

# 문제는 어떻게 하느냐.. q를 이용??
# 오른쪽 [[0,1],[1,0],[0,-1],[1,0]]
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
matrix = [[0]*N for _ in range(N)] 
for _ in range(int(input())):
    a,b = map(int,input().split())
    matrix[a-1][b-1] = 1
rotate = {}
for _ in range(int(input())):
    time,cmd = input().split()
    rotate[int(time)] = cmd
xy = [[0,1],[1,0],[0,-1],[-1,0]]
time = 1
snake = deque([[0,0,0]]) # row,col,direction
matrix[0][0] = - 1
# 몸통만 저장해두고.
# 사과 없으면 꼬리pop() & direction 지정해서 몸통 append

while True:
    head,d = snake[-1][:2],snake[-1][2] # row,col만
    head[0] += xy[d][0]
    head[1] += xy[d][1]
    if 0<= head[0] <N and 0<=head[1] <N and matrix[head[0]][head[1]] != -1: # 몸통 & 범위 밖아님
        if matrix[head[0]][head[1]]: # 사과있음
            pass
        else:
            x,y,_ = snake.popleft()
            matrix[x][y] = 0
        matrix[head[0]][head[1]] = -1
        if time in rotate:
            if rotate[time] == 'L': # 왼쪽 회전
                d = (d-1) % 4
            else: # 오른쪽 회전
                d = (d+1) % 4
        time += 1
        snake.append([head[0],head[1],d])
    else:
        print(time)
        break


