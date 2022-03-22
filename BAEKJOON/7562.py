import sys
import collections
def bfs():
    stack = collections.deque([[current[0], current[1]]])
    while stack and not matrix[target[0]][target[1]]: # target 이랑  current랑 같으면? 이건 그냥 함수 보내기 전에 생각
        for _ in range(len(stack)):
            row, col = stack.pop()
            dx = [1,1,2,2,-1,-1,-2,-2]
            dy = [2,-2,1,-1,-2,2,-1,1]
            for i in range(len(dx)):
                r = dx[i] + row
                c = dy[i] + col
                if 0<= r < len(matrix) and 0<= c < len(matrix) and matrix[r][c] == 0:
                    matrix[r][c] = matrix[row][col] + 1 # 변수 명을 잘 정하자.. 십.. 내시간
                    stack.appendleft([r,c])

for _ in range(int(sys.stdin.readline())):
    size = int(sys.stdin.readline())
    current = list(map(int, sys.stdin.readline().split()))
    target = list(map(int, sys.stdin.readline().split()))
    matrix = [[0 for _ in range(size)]for _ in range(size)]
    if target != current:
        bfs()
    print(matrix[target[0]][target[1]])
