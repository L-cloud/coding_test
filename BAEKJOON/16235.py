from typing import List 
from collections import defaultdict,deque
import sys
input = sys.stdin.readline
def spring(trees:dict[List[int]],land:List[List[int]]) -> List[List[int]]:
    d_t = []
    b = []
    for key in trees:
        for i,t in enumerate(trees[key]):
            if t <= land[key[0]][key[1]]:
                land[key[0]][key[1]] -= t
                trees[key][i] += 1
                if trees[key][i] % 5 == 0:
                    b.append(key)
            else:
                for _ in range(len(trees[key]) - i): # 몇 그루가 살아남았나
                    land[key[0]][key[1]] += trees[key].pop() // 2
                break
    return b


def fall(b:List[int],trees:dict[List[int]], N:int) -> None:
    dx = [-1,1,0,0,1,1,-1,-1]
    dy = [0,0,1,-1,1,-1,1,-1]
    tempt = []
    for row,col in b:
        for k in range(8):
            x = dx[k] + row
            y = dy[k] + col
            if 0<= x < N and 0<= y < N:
                trees[(x,y)].appendleft(1)
    return

def winter(original:List[List[int]], land:List[List[int]]) ->None :
    for i in range(len(land)):
        for j in range(len(land)):
            land[i][j] += original[i][j]
    return
    
N, M, K = map(int, input().split())
trees  = defaultdict(deque)
original = [list(map(int,input().split()))for _ in range(N)] # 원래 영양분
land = [[5]*N for i in range(N)] # 현재 영양분
for _ in range(M):
    a,b,c = map(int,input().split())
    trees[(a-1,b-1)].append(c)
for _ in range(K):
    if not trees:
        print(0)
        exit()
    b = spring(trees, land) # 죽은 나무 영양분 return
    fall(b,trees,N)
    winter(original,land)

print(sum(len(trees[key]) for key in trees))
