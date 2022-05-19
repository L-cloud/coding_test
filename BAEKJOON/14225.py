import sys, itertools

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
v = [False for _ in range(sum(num_list) + 2)]
for i in range(1,N+1):
    for n in itertools.combinations(num_list,i):
        v[sum(n)] = True

print(v[1:].index(False) + 1)
