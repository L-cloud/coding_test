from typing import List, Union
def roate(c:List[int],d:int, k:int, x:int) -> None:
    # 돌리는 함수. 지워야하는 로직 있으니 일단 돌리기만! + M // 2 보다 더 크면 M - M//2이 로직도 밖에서 해주자! while 문도 밖에서!
    if d: # 반시계방향
        while k:
            c[x] = [c[x][(i+1) % len(c[x])] for i in range(len(c[x]))]
            k -= 1
    while k:
        c[x] = [c[x][(i-1) % len(c[x])] for i in range(len(c[x]))]
        k -= 1


def erase(c:List[int]) -> Union[List[List[int]], bool]:
    n_c,flag = [[c[i][j] for j in range(len(c[0]))] for i in range(len(c))], False
    for i in range(len(c)):
        for j in range(len(c[0])):
            if c[i][j]:
                if c[i][(j-1)%len(c[0])] == c[i][j]:
                    n_c[i][j], n_c[i][(j-1)%len(c[0])] = 0,0
                    flag = True
                if  c[i][(j+1)%len(c[0])] == c[i][j]:
                    n_c[i][j], n_c[i][(j+1)%len(c[0])] = 0,0
                    flag = True
                if 0<i and c[i][j] == c[i-1][j]:
                    n_c[i][j], n_c[i-1][j] = 0,0
                    flag = True
                if i < len(c) - 1 and c[i][j] == c[i+1][j]:
                    n_c[i][j], n_c[i+1][j] = 0,0
                    flag = True
    return n_c, flag

def get_average(c:List[int]) -> float:
    '''
    아 꼼꼼히 생각하자.. 모두 0인데 get_average 들어올 수 있음..!!
    '''
    cnt, n = 0,0
    for i in range(len(c)):
        for j in range(len(c[0])):
            if c[i][j]:
                cnt += c[i][j]
                n += 1
    return cnt / n if n else 0


import sys
input = sys.stdin.readline
N,M,T = map(int,input().split()) # 반지름, 각 원판의 수, 회전 횟수
circle = [list(map(int, input().split())) for _ in range(N)]
for _ in range(T):
    x,d,k = map(int,input().split()) # x의 배수인 녀석들 d 방향 k번 회전
    if k > M // 2:
        k = M - k
        d = 0 if d else 1
    i = 1
    while x * i <= N:
        roate(circle,d,k,x*i-1)
        i += 1
    circle, flag = erase(circle)
    if not flag:
        av = get_average(circle)
        for i in range(N):
            for j in range(M):
                if circle[i][j] and circle[i][j] > av:
                    circle[i][j] -= 1
                elif circle[i][j] and circle[i][j] < av:
                    circle[i][j] += 1
print(sum([circle[i][j] for i in range(N) for j in range(M)]))
