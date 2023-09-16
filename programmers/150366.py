from typing import List
def solution(commands:List[str]) -> List[str]:
    index_cell = [[[i,j] for j in range(50)] for i in range(50)]
    cell = [["EMPTY"] * 50 for _ in range(50)]
    answer = []
    for cmd in commands:
        cmd = cmd.split()
        if cmd[0] == "UPDATE": 
            if len(cmd) == 3: update1(cell, cmd[1], cmd[2])
            else: update2(index_cell,cell, int(cmd[1]) -1, int(cmd[2]) -1, cmd[3])
        elif cmd[0] == "MERGE": 
            merge(index_cell, cell, int(cmd[1]) -1, int(cmd[2]) -1 , int(cmd[3]) -1 , int(cmd[4]) -1)
        elif cmd[0] == "UNMERGE":
            unmerge(index_cell,cell, int(cmd[1]) -1 ,int(cmd[2]) -1)
        else:
            answer.append(cell[int(cmd[1])-1][int(cmd[2]) -1])
    return answer

# 고민 -> 이걸 굳이 cell 모두 바꿀 필요가 있나..? 흠.. 일단 가지고 있는게 나을듯? 복잡성을 위해
def update1(cell:List[List[str]] , v1:str, v2:str):
    for i in range(50):
        for j in range(50):
            if cell[i][j] == v1: cell[i][j] = v2
            
def update2(index_cell:List[List[int]],cell:List[List[str]] , r:int, c:int, v:str ):
    for i in range(50):
        for j in range(50):
            if index_cell[i][j] == index_cell[r][c]: cell[i][j] = v

def merge(index_cell :List[List[int]], cell :List[List[str]],r1:int,c1:int,r2:int,c2:int):
    if index_cell[r1][c1] == index_cell[r2][c2]: return
    v = cell[r1][c1] if cell[r1][c1] != "EMPTY" else cell[r2][c2]
    index = index_cell[r2][c2]
    for i in range(50):
        for j in range(50):
            if index_cell[i][j] == index or index_cell[i][j] == index_cell[r1][c1] : 
                index_cell[i][j] = index_cell[r1][c1]  # merge
                cell[i][j] = v # 값 변경

def unmerge(index_cell :List[List[int]], cell :List[List[str]],r:int,c:int):
    v = cell[r][c]
    rc = index_cell[r][c]
    for i in range(50):
        for j in range(50):
            if index_cell[i][j] == rc: 
                cell[i][j] = "EMPTY"
                index_cell[i][j] = [i,j]
    cell[r][c] = v
