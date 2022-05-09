import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
max_sum = 0

for i in range(N):
    tempt = 0
    for j in range(i):
        if num[j] < num[i]:
            tempt += num[j]
    max_sum = max(max_sum, tempt+num[i])

print(max_sum)