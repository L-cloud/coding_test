import sys

number = sys.stdin.readline()
num_list = list(map(int, sys.stdin.readline().split()))
demical = 0
for num in num_list:
    i, flag = 2, True
    while i*i <= num:
        if num % i == 0:
            flag = False
            break
        i += 1
    if flag and 2 <= num:
        demical += 1
print(demical)
    