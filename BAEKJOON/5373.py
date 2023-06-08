import sys
from typing import List
from copy import deepcopy
input = sys.stdin.readline

def nine(c:List[List[str]], d:int) -> List[List[str]]:
    while d:
        c = [list(i) for i in zip(*c[::-1])]
        d -= 1
    return c
def roate(cube:List[List[List[str]]], d:str) -> List[List[List[str]]]:
    c = deepcopy(cube)
#    print("before ", c)
    # 기준을 어떻게 할 것이냐를 정확히 세우자

    '''
    앞,뒤   123
        456
        789
    오른쪽은 앞의 3에 이어진게 1 123 왼쪽도 동일하게 
    '''
    if d == "U+":
        # 오 -> 앞 -> 왼 -> 뒤
        c[3][0] = cube[1][0][::] # 앞 = 오
        c[2][0] = cube[3][0][::-1] # 왼 = 앞 바뀜
        c[4][0] = cube[2][0][::] # 뒤 = 왼
        c[1][0] = cube[4][0][::-1] # 오 = 뒤 바뀜
        c[0] = nine(cube[0], 1)
    elif d == "U-":
        # 오 -> 뒤 -> 왼 -> 앞
        c[4][0] = cube[1][0][::-1] #  뒤 = 오 바뀜
        c[2][0] = cube[4][0][::] # 왼 = 뒤
        c[3][0] = cube[2][0][::-1] # 앞 = 왼 바뀜
        c[1][0] = cube[3][0][::] # 오 = 앞
        c[0] = nine(cube[0], 3)
    elif d == "D-":
        c[3][-1] = cube[1][-1][::]  # 앞 = 오
        c[2][-1] = cube[3][-1][::-1]  # 왼 = 앞 바뀜
        c[4][-1] = cube[2][-1][::]  # 뒤 = 왼
        c[1][-1] = cube[4][-1][::-1]  # 오 = 뒤 바뀜
        c[5] = nine(cube[5], 1)
    elif d == "D+":
        # 오 -> 뒤 -> 왼 -> 앞 -> 오
        c[4][-1] = cube[1][-1][::-1] # 뒤 = 오 바뀜
        c[2][-1] = cube[4][-1][::]# 왼 = 뒤
        c[3][-1] = cube[2][-1][::-1] # 앞 = 왼 바뀜
        c[1][-1] = cube[3][-1][::] # 오 = 앞
        c[5] = nine(cube[5], 3)
    # 바뀌는거 기준을 정해줘야함.. 일단 ㅇㅋ
    elif d== "B-":
        # 위 -> 오 -> 아래 -> 왼
        c[1][0][2],c[1][1][2],c[1][2][2] = cube[0][0][0], cube[0][0][1], cube[0][0][2] # 오 = 위
        c[5][0][0], c[5][0][1], c[5][0][2] = cube[1][2][2],cube[1][1][2],cube[1][0][2] # 아래 = 오 바뀜
        c[2][0][2], c[2][1][2], c[2][2][2] = cube[5][0][0], cube[5][0][1], cube[5][0][2] # 왼 = 아래
        c[0][0][0], c[0][0][1], c[0][0][2] = cube[2][2][2], cube[2][1][2], cube[2][0][2] # 위 = 왼 바뀜
        c[4] = nine(cube[4],1)
    elif d== "B+":
        # 위 ->왼 -> 아래 -> 오
        c[2][0][2], c[2][1][2], c[2][2][2] =  cube[0][0][2], cube[0][0][1], cube[0][0][0] # 왼 = 위 바뀜
        c[5][0][0], c[5][0][1], c[5][0][2] = cube[2][0][2], cube[2][1][2], cube[2][2][2]  # 아래 = 왼
        c[1][0][2], c[1][1][2], c[1][2][2] = cube[5][0][2], cube[5][0][1], cube[5][0][0] # 오 = 아래 바뀜
        c[0][0][0], c[0][0][1], c[0][0][2] =  cube[1][0][2], cube[1][1][2], cube[1][2][2]# 위 = 오
        c[4] = nine(cube[4], 3)
    elif d == "F+":
        # 위 -> 오 -> 아래 -> 왼
        c[1][0][0],c[1][1][0],c[1][2][0] = cube[0][2][0], cube[0][2][1], cube[0][2][2] # 오 = 위
        c[5][2][0], c[5][2][1], c[5][2][2] = cube[1][2][0],cube[1][1][0],cube[1][0][0] # 아래 = 오 바뀜
        c[2][0][0], c[2][1][0], c[2][2][0] = cube[5][2][0], cube[5][2][1], cube[5][2][2] # 왼 = 아래
        c[0][2][0], c[0][2][1], c[0][2][2] =  cube[2][2][0], cube[2][1][0], cube[2][0][0] # 위 = 왼 바
        c[3] = nine(cube[3], 1)
    elif d == "F-":
        # 위 -> 왼 -> 아래 -> 오
        c[2][0][0], c[2][1][0], c[2][2][0] = cube[0][2][2], cube[0][2][1], cube[0][2][0] # 왼 = 위 바뀜
        c[5][2][0], c[5][2][1], c[5][2][2] = cube[2][0][0], cube[2][1][0], cube[2][2][0]# 아래 = 왼
        c[1][0][0],c[1][1][0],c[1][2][0] = cube[5][2][2], cube[5][2][1], cube[5][2][0]# 오 = 아래  바뀜
        c[0][2][0], c[0][2][1], c[0][2][2] = cube[1][0][0],cube[1][1][0],cube[1][2][0]# 위 = 오
        c[3] = nine(cube[3], 3)
    elif d == "R+":
        # 위 -> 뒤 -> 아래 -> 앞
        c[4][0][2], c[4][1][2], c[4][2][2] = cube[0][2][2], cube[0][1][2], cube[0][0][2] # 뒤 = 위 바뀜
        c[5][0][2],c[5][1][2],c[5][2][2] = cube[4][0][2], cube[4][1][2], cube[4][2][2] #아래 = 뒤
        c[3][0][2], c[3][1][2], c[3][2][2] = cube[5][2][2],cube[5][1][2],cube[5][0][2] # 앞 = 아래 바뀜
        c[0][0][2], c[0][1][2], c[0][2][2] = cube[3][0][2], cube[3][1][2], cube[3][2][2] # 위 = 앞
        c[1] = nine(cube[1], 1)

    elif d == "R-":
        # 위 -> 앞 -> 아래 -> 뒤
        c[3][0][2], c[3][1][2], c[3][2][2] = cube[0][0][2], cube[0][1][2], cube[0][2][2] # 앞 = 위
        c[5][0][2], c[5][1][2], c[5][2][2] = cube[3][2][2], cube[3][1][2], cube[3][0][2] # 아래 = 앞 바뀜
        c[4][0][2], c[4][1][2], c[4][2][2] = cube[5][0][2], cube[5][1][2], cube[5][2][2] # 뒤 = 아래
        c[0][0][2], c[0][1][2], c[0][2][2] = cube[4][2][2], cube[4][1][2], cube[4][0][2]# 위 = 뒤 바뀜
        c[1] = nine(cube[1], 3)
    elif d == "L+":
        # 위 -> 앞 -> 아래 -> 뒤
        c[3][0][0], c[3][1][0], c[3][2][0] = cube[0][0][0], cube[0][1][0], cube[0][2][0] # 앞 = 위
        c[5][0][0], c[5][1][0], c[5][2][0] = cube[3][2][0], cube[3][1][0], cube[3][0][0] # 아래 = 앞 바뀜
        c[4][0][0], c[4][1][0], c[4][2][0] = cube[5][0][0], cube[5][1][0], cube[5][2][0] # 뒤 = 아래
        c[0][0][0], c[0][1][0], c[0][2][0] = cube[4][2][0], cube[4][1][0], cube[4][0][0]# 위 = 뒤 바뀜
        c[2] = nine(cube[2], 3)
    elif d == "L-":
        # 위 -> 뒤 -> 아래 -> 앞
        c[4][0][0], c[4][1][0], c[4][2][0] = cube[0][2][0], cube[0][1][0], cube[0][0][0]  # 뒤 = 위 바뀜
        c[5][0][0], c[5][1][0], c[5][2][0] = cube[4][0][0], cube[4][1][0], cube[4][2][0]  # 아래 = 뒤
        c[3][0][0], c[3][1][0], c[3][2][0] = cube[5][2][0], cube[5][1][0], cube[5][0][0]  # 앞 = 아래 바뀜
        c[0][0][0], c[0][1][0], c[0][2][0] = cube[3][0][0], cube[3][1][0], cube[3][2][0]  # 위 = 앞
        c[2] = nine(cube[2], 1)
    return c



for _ in range(int(input())):
    # 위 0, 오른쪽 1, 왼쪽 2, 앞 3, 뒤 4, 아래 5
    cube = [[['w'] * 3 for _ in range(3)],
            [['b'] * 3 for _ in range(3)],
            [['g'] * 3 for _ in range(3)],
            [['r'] * 3 for _ in range(3)],
            [['o'] * 3 for _ in range(3)],
            [['y'] * 3 for _ in range(3)]]

    N = int(input())
    cmd = input().split()
    for c in cmd:
        cube = roate(cube,c)
    for i in cube[0]:
        print(''.join(i))
