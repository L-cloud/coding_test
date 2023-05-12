import sys
from collections import Counter
input = sys.stdin.readline
total = [0 for _ in range(int(input()))]
for _ in range(3):
    rates, order = list(map(int,input().split())), {}
    total = [total[i] + rates[i] for i in range(len(rates))]
    cnt, r = sorted(Counter(rates).items(), reverse = True), 1 
    for k,v in cnt:
        order[k] = r
        r += v
    print(' '.join([str(order[r]) for r in rates]))
order = {}
cnt, r = sorted(Counter(total).items(), reverse = True), 1
for k,v in cnt:
    order[k] = r
    r += v
print(' '.join([str(order[r]) for r in total]))
