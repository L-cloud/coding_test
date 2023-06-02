import sys
from typing import List
def rotate(matrix:List[List[int]],index:int, direction:int) -> None:
    tempt = [matrix[index][(i + 1) % 8] for i in range(8)] if direction == -1 else [matrix[index][i - 1] for i in range(8)]
    matrix[index] = tempt

def which_one(matrix:List[List[int]], index:int, direction:int) -> List[int]:
    # 왼쪽 따로 오른쪽 따로 해줘야하는구나!
    r = [[index,direction]]
    i, d = index, direction
    while -1 <  i - 1: # 왼쪽
        if matrix[i-1][2] != matrix[i][6]:
            r.append([i-1,-d])
            d = -d
            i -= 1
        else:
            break
    i, d = index, direction
    while i + 1 < 4:
        if matrix[i+1][6] != matrix[i][2]:
            r.append([i+1,-d])
            i += 1
            d = -d
        else:
            break
    return r
input = sys.stdin.readline
matrix = [input().strip() for _ in range(4)]
matrix = [[int(i) for i in matrix[j]] for j in range(4)]
for _ in range(int(input())):
    index, direction = map(int,input().split())
    r = which_one(matrix,index-1,direction)
    for i, d in r:
        rotate(matrix,i,d)
cnt = 0
for i in range(4):
    cnt += ((2**i) * matrix[i][0])
print(cnt)
