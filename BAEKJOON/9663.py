import time
N = int(input())

ans = [0]
row = [0 for _ in range(N)]

def queen(x):
    for i in range(x):
        # 가로 확인 // 대각선 확인
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    
    return True

def n_queens(x):
    if x == N:
        ans[0] += 1
        return
    else:
        for i in range(N):
            # [x, i]에 퀸을 놓음
            row[x] = i
            if queen(x):
                n_queens(x+1)
a = time.time()
n_queens(0)
print(ans[0], time.time() - a)