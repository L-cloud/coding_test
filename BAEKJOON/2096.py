import sys
input = sys.stdin.readline
N = int(input())
dp_max = list(map(int,input().split()))
dp_min = dp_max[:]
for _ in range(N -1):
    a,b,c = map(int,input().split())
    dp_max[0], dp_max[1], dp_max[2] = max(dp_max[:2]) + a, max(dp_max) + b, max(dp_max[1:]) + c
    dp_min[0], dp_min[1], dp_min[2] = min(dp_min[:2]) + a, min(dp_min) + b, min(dp_min[1:]) + c
print(max(dp_max), min(dp_min))