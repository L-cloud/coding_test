from typing import List
def solution(key:List[int], lock:List[int]):
    k_l,l_l,s = len(key), len(lock),sum([sum(i) for i in lock])
    matrix = [[0] *(2*k_l + l_l) for _ in range(2*k_l + l_l)]
    for i in range(l_l):
        for j in range(l_l):
            matrix[k_l+i][k_l+j] = lock[i][j]
    for i in range(4):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if docking(i,j,key,matrix,s,len(lock)):
                    return True
        key = rotate(key)
    return False

def rotate(key:List[int]) -> List[int]:
    s = [[0]*len(key) for _ in range(len(key))]
    for i in range(len(key)):
        for j in range(len(key)):
             s[j][len(key)-i-1] = key[i][j]
    return s

def docking(i:int, j:int, key:List[int], lock:List[int],s:int,c:int) -> bool: # s는 현재, c는 길이
    for x_i in range(len(key)):
        for y_i in range(len(key)):
            if len(key)<=x_i + i< len(key) + c and len(key)<= y_i +j <len(key) +c : # 일단 범위 내
                if key[x_i][y_i] : # 돌기 있음
                    if lock[x_i + i][y_i +j]:
                        return False
                    else:
                        s += 1
    return s == c*c
