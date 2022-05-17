import sys,itertools
N, S = map(int, sys.stdin.readline().split())

num_list = list(map(int, sys.stdin.readline().split()))
vis = set()
cnt = 0

for i in range(1,N + 1):
    num = list(itertools.combinations(num_list,i))
    for n in num:
        if S == sum(n):
            cnt += 1
print(cnt)
