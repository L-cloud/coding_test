import sys

input = sys.stdin.readline
N,K = map(int,input().split())
belt = list(map(int,input().split()))
robot = [False] * N
ans,cnt = 0,0
while cnt < K:
    ans += 1
    belt = [belt[(i-1) % (N * 2)] for i in range(N*2)]
    robot = [robot[(i-1) % N] for i in range(N)]
    if robot[N-1]: # 내리는 위치인 경우 즉시 내림
        robot[N-1] = False
    r = [i for i,v in enumerate(robot) if v]
    for i in r[::-1]:
        if i == N - 2 and belt[N-1]:
            robot[i] = False
            belt[N-1] -= 1
            cnt += 1 if not belt[N-1] else 0
        else:
            if belt[i + 1] and not robot[i + 1]:
                robot[i] = False
                robot[i+1] = True
                belt[i + 1] -= 1
                cnt += 1 if not belt[i + 1] else 0
    if belt[0] and not robot[0]:
        belt[0] -= 1
        cnt += 1 if not belt[0] else 0
        robot[0] = True
print(ans)
