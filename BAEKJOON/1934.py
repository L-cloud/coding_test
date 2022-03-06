import sys

for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    max_factor = max(a, b)
    tempt_min = min(a, b)
    tempt = max_factor
    while True:
        if max_factor % tempt_min == 0:
            max_factor = tempt_min
            break
        else:
            tempt = max_factor
            max_factor = tempt_min 
            tempt_min = tempt % max_factor
    print(int(a * b / max_factor))


