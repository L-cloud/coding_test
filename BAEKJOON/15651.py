import sys
import itertools

a, b = map(int,sys.stdin.readline().split())
per = list(itertools.product(range(1, a+1), repeat =b))

for i in sorted(per):
    print(*i)