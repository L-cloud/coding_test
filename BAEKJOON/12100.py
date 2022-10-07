# 한 번의 이동에서 이미합쳐진 블록은 또 다른 블록과 다시 합쳐질 수 없다.

# 400 * 2**10 102400 40만 흐음 # 달라진거 있으면 다음꺼로 넘김 

# origin을 일단 복사 해야겠지? 중복 처리도 해줘야함 일단 그냥 해보자


import sys
import tabnanny
from typing import List
import copy
input = sys.stdin.readline
N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]
answer = 0
# 이거 잘못하면 시간초과다.
def left(matrix:List[List[int]])->bool:
    global answer
    v = set() # 합쳐지는 배열 선택
    max_num = 0 
    flag= False
    for i in range(len(matrix)):
        for j in range(1,len(matrix)):
            t = matrix[i][j]
            if t:
                while 0 < j and not matrix[i][j -1]:
                    matrix[i][j] = 0
                    j -= 1  
                    matrix[i][j] = t
                    flag = True
                if  0< j and matrix[i][j-1] == t and (i,j-1) not in v:
                    v.add((i,j-1)) 
                    matrix[i][j] = 0
                    matrix[i][j-1] *= 2
                    max_num = max(max_num,matrix[i][j-1])
    answer  = max(answer, max_num)
    return flag  # 바뀌었는지 안 바뀌었는지 확인
                
def up(matrix:List[List[int]]) -> bool:
    global answer
    v = set() # 합쳐지는 배열 선택
    flag = False
    max_num = 0 
    for i in range(1,len(matrix)):
        for j in range(len(matrix)):
            t = matrix[i][j]
            if t:
                while 0 < i and not matrix[i -1][j]:
                    matrix[i][j] = 0
                    i -= 1  
                    matrix[i][j] = t
                    flag = True
                if  0 < i and  matrix[i-1][j] == t and (i-1,j) not in v:
                    v.add((i-1,j)) 
                    matrix[i][j] = 0
                    matrix[i-1][j] *= 2
                    max_num = max(max_num,matrix[i-1][j])
    answer  = max(answer, max_num)
    return flag  

def down(matrix:List[List[int]]) -> bool:
    global answer 
    v = set() # 합쳐지는 배열 선택
    flag = False
    max_num = 0 
    for i in range(len(matrix)-2,-1,-1):
        for j in range(len(matrix)):
            t = matrix[i][j]
            if t:
                while i < len(matrix) -1 and not matrix[i+1][j]:
                    matrix[i][j] = 0
                    i += 1
                    matrix[i][j] = t
                    flag = True
                if i < len(matrix) - 1 and matrix[i+1][j] == t and (i+1,j) not in v:
                    v.add((i+1,j))
                    matrix[i][j] = 0
                    matrix[i+1][j] *= 2
                    max_num = max(max_num,matrix[i+1][j])
    answer  = max(answer, max_num)
    return flag

def right(matrix:List[List[int]]) -> bool:
    global answer
    v = set()
    flag = False
    max_num = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)-2,-1,-1):
            t = matrix[i][j]
            if t:
                while j < len(matrix) -1 and not matrix[i][j+1]:
                    matrix[i][j] = 0
                    j += 1
                    matrix[i][j] = t
                    flag = True
                if j < len(matrix) -1 and matrix[i][j+1] == t and (i,j+1) not in v:
                    v.add((i,j+1))
                    matrix[i][j] = 0
                    matrix[i][j+1] *= 2
                    max_num = max(max_num,matrix[i][j+1])
    answer = max(answer, max_num)
    return flag

func = {0:right,1:down,2:left,3:up}
def dfs(matrix:List[List[int]], cnt:int) -> None:
    if 5 < cnt:
        return 
    for i in range(4):
        t = copy.deepcopy(matrix)
        if func[i](t) :
            dfs(t,cnt + 1)
dfs(matrix,1)
print(answer)
