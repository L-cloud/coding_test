'''
경사로는 낮은 칸에 놓으며, L개의 연속된 칸에 경사로의 바닥이 모두 접해야 한다.
낮은 칸과 높은 칸의 높이 차이는 1이어야 한다.
경사로를 놓을 낮은 칸의 높이는 모두 같아야 하고, L개의 칸이 연속되어 있어야 한다.
'''



N,L = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
def check_row(index:int,N:int,L:int)->bool:
    left,right  = 0,1
    v=set() # 경사로
    while right < N:
        if matrix[index][left] == matrix[index][right]:
            left += 1
            right += 1
        elif matrix[index][left] + 1 == matrix[index][right]: # 오른쪽이 1 더 큼
            t,l_index = left,L
            while l_index:
                if -1< t and matrix[index][left] == matrix[index][t] and t not in v:
                    v.add(t)
                    l_index -= 1
                    t -= 1
                else:
                    return False
            left += 1
            right += 1
        elif  matrix[index][left] == matrix[index][right] + 1: # 왼쪽 1 더 큼
            t,l_index = right,L
            while l_index:
                if t < N and matrix[index][right] == matrix[index][t] and t not in v:
                    v.add(t)
                    l_index -= 1
                    t += 1
                else:
                    return False
            right = t
            left = t -1
        else:
            return False
    return True

def check_col(index:int,N:int,L:int) -> bool:
    left,right = 0,1
    v = set()
    while right < N:
        if matrix[left][index] == matrix[right][index]:
            left += 1
            right += 1
        elif matrix[left][index] + 1 == matrix[right][index] : # 오른쪽이 1 더 큼
            t,l_index = left,L 
            while l_index:
                if -1< t and matrix[left][index] == matrix[t][index] and t not in v:
                    v.add(t)
                    l_index -= 1
                    t -= 1
                else:
                    return False
            left += 1
            right += 1
        elif  matrix[left][index] == matrix[right][index] + 1: # 왼쪽 1 더 큼
            t,l_index = right,L
            while l_index:
                if t < N and matrix[right][index] == matrix[t][index] and t not in v:
                    v.add(t)
                    l_index -= 1
                    t += 1
                else:
                    return False
            right = t 
            left = t-1
        else:
            return False
    return True

ans = 0
for i in range(N):
    ans += check_row(i,N,L)
    ans += check_col(i,N,L)
print(ans)
