import sys
import itertools

dwarf = [0] * 9
for i in range(9):
    dwarf[i] = int(sys.stdin.readline())

combi = itertools.combinations(dwarf, 7)
for c in combi:
    print(c)
    if sum(c) == 100:
        for d in sorted(c):
            print(d)
        exit()