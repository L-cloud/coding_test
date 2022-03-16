import sys

num = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
max_num = float('-inf')
total = 0
for n in num_list:
    total += n
    max_num = max(total, max_num)
    if total < 0:
        total = 0

print(max_num)
