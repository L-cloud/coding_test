import sys
from functools import reduce
input = sys.stdin.readline
n,m = map(int,input().split())
plus, multi = sorted(list(map(int,input().split()))),sorted(list(map(int,input().split())))
print(((lambda x: sum(plus) * (x if x else 1))(reduce(lambda x,y: x*y, filter(lambda x: x, multi), 1))))
