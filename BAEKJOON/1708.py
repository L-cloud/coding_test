import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split()))for _ in range(N)]
cnt = {-1 : 0, 0 : 0, 1: 0}

def count_paper(paper):
    size = len(paper)
    zero = [[0 for _ in range(size)] for _ in range(size)]
    one = [[1 for _ in range(size)] for _ in range(size)]
    minus = [[-1 for _ in range(size)] for _ in range(size)]
    if paper == zero:
        cnt[0] += 1
        return
    elif paper == one:
        cnt[1] += 1
        return
    elif paper == minus:
        cnt[-1] += 1
        return
    if size == 3: # 더 못 나눔
        for i in range(3):
            for j in range(3):
                cnt[paper[i][j]] += 1
    else: # 분할 해야함
        size = size // 3
        for i in range(3): # 가로 세로 둘 다 나눠야함
            for j in range(3):
                p = [paper[k + i*size][j*size : (j+1) * size] for k in range(size)]
                print(p)
                count_paper(p)
count_paper(paper)
for key in [-1,0,1]:
    print(cnt[key])