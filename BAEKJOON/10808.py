import sys
import collections

cnt = collections.Counter('abcdefghijklmnopqrstuvwxyz')

alpha = sys.stdin.readline().strip()

for a in alpha:
    cnt[a] += 1

for key in 'abcdefghijklmnopqrstuvwxyz':
    print(cnt[key] - 1, end = " ")