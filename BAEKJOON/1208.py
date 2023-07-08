import sys,itertools
from collections import Counter
N, S = map(int, sys.stdin.readline().split())

num_list = list(map(int, sys.stdin.readline().split()))
left = num_list[:len(num_list) // 2]
right = num_list[len(num_list) // 2:]
l_c, r_c = Counter(),Counter()

for i in range(1,len(left)+1):
    for n in itertools.combinations(left,i):
        l_c[sum(n)] += 1

for i in range(1,len(right) + 1):
    for n in itertools.combinations(right,i):
        r_c[sum(n)] += 1 
cnt = l_c[S] + r_c[S]
for k,v in l_c.items():
    cnt += r_c[S-k]*v
print(cnt)

