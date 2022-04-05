import itertools, sys

N = int(sys.stdin.readline())

for i in itertools.permutations(range(1,N+1), N):
    print(*i)